'''
Author - Parth Chudasama
Desc - Main flask app
'''

import io
import os
import re
import zipfile
import requests
import sys
import shutil
import logging
import eventlet
from os.path import basename
from pathlib import Path
from pprint import pprint
from flask_cors import CORS
from google.cloud import vision
from spellchecker import SpellChecker
from google.cloud.vision import types
from OCR import vision_ocr, processed_ocr
from werkzeug.utils import secure_filename
from preprocessing import image_preprocessing
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify, request, session, render_template, send_file
from report import *


app = Flask(__name__, template_folder="templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Enble Cors
CORS(app)

socketio = SocketIO(app, cors_allowed_origins='*')
# check if dir exist & if not create one

DEBUG = False


def check_create_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return None


def dstore_delete():
    print('Deleteting .DSstore')
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.DS_Store'):
                path = os.path.join(root, file)

                print("Deleting: %s" % (path))

                if os.remove(path):
                    print("Unable to delete!")
                else:
                    pass
    print('Deleted .DSstore')
    return None


# Disables GET POST logs
log = logging.getLogger('socketio')
log.disabled = True
log1 = logging.getLogger('engineio')
log1.disabled = True

# setting GCP creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret_key.json"

# Check and create required folders
student_upload = os.getcwd() + '/student_files'
check_create_dir(student_upload)
misc_files = os.getcwd() + '/misc_files'
check_create_dir(misc_files)
preprocessed = os.getcwd() + '/preprocessed'
check_create_dir(preprocessed)
dstore_delete()

# PATH_PAPERS = preprocessed
PATH_ANSKEY = os.getcwd() + '/misc_files/master_file.txt'
PATH_PAPERS = os.getcwd() + '/preprocessed'


@app.route('/')
def index():
    return render_template("index.html")

# Testing purpose
@app.route('/test', methods=['GET'])
def test():
    socketio.emit('text_response',
                  {'data': str('false')})

    return None


def spell_correction(text):
    correction = []
    spell = SpellChecker()
    spell.word_frequency.load_text_file(misc_files+'/correction_file.txt')
    word_list = list(text.split(" "))
    for word in word_list:
        correction.append(spell.correction(word))
    corr_text = ' '.join(correction)
    return corr_text

# remove dirs **only testing phase


def delete_dir(mydir):
    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    return None

# get student file and save in student_files dir
@app.route('/student-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part`
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    files = request.files.getlist('file')
    if files:
        if not os.path.isdir('student_files'):
            os.mkdir('student_files')

        for file in files:
            filename = secure_filename(file.filename)
            ext = filename.split('.')[-1]
            file_name = 'student_{}.{}'.format(files.index(file), ext)
            file.save(os.path.join(student_upload, file_name))
            resp = jsonify({'message': 'File successfully uploaded'})
            # text = 'FILE UPLAODEED'
            # pprint(text)
            # socketio.emit('text_response',
            #               {'data': str(text)})
            resp.status_code = 200
        return resp

# get master and correction file
@app.route('/master-upload', methods=['POST'])
def master_file():
    # check if the post request has the file part`
    if ('master' not in request.files) and ('correction' not in request.files):
        print('no file')
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    master_file = request.files.get('master')

    if master_file:
        if not os.path.isdir('misc_files'):
            os.mkdir('misc_files')
        # for master
        master_filename = secure_filename(master_file.filename)
        master_ext = master_filename.split('.')[-1]
        master_name = 'master_file.{}'.format(master_ext)
        master_file.save(os.path.join(misc_files, master_name))

        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 200
        return resp


@app.route('/correct-upload', methods=['POST'])
def correct_file():
    if 'correction' not in request.files:
        print('no file')
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    autocorrect = request.files.get('correction')
    if autocorrect:
        if not os.path.isdir('misc_files'):
            os.mkdir('misc_files')
        correction_filename = secure_filename(autocorrect.filename)
        correction_ext = correction_filename.split('.')[-1]
        if correction_ext != 'txt':
            print('Text file not found for autocorrection, kindly change format')
        correction_name = 'correction_file.{}'.format(correction_ext)
        autocorrect.save(os.path.join(misc_files, correction_name))
        resp = jsonify({'message': 'File successfully uploaded'})
        if not DEBUG:
            pre = image_preprocessing(student_upload, preprocessed)
            pre.check_for_file_formats_and_process()

            if (os.path.isdir("preprocessed/S1") and os.path.isdir("preprocessed/PHOTOS")):
                ocr_path = 'preprocessed'
                dir_flag = 'multiple'
                print('\n\nUser has uploaded different formats')
            elif os.path.isdir("preprocessed/PHOTOS"):
                ocr_path = 'preprocessed/PHOTOS'
                dir_flag = 'photo'
                print("\n\nUser has uploaded images")
            elif os.path.isdir("preprocessed/S1"):
                ocr_path = 'preprocessed'
                dir_flag = 'pdf'
                print('\n\nUser has uploaded pdf')

            if dir_flag is None:
                print('FATAL ERROR, RESTART')
            handler = processed_ocr(dir_flag)
            if dir_flag == 'photo':
                handler.image_handle(ocr_path)
                print('OCR results saved in PHOTOS')
            if dir_flag == 'pdf':
                handler.pdf_handle(ocr_path)
                print('OCR results saved in preprocessed')

            if dir_flag == 'multiple':
                handler.multiple_handler(ocr_path)
                print('OCR results saved in respective folder')
        dstore_delete()
        marks, reference_answers = process_answer_key(PATH_ANSKEY)
        all_student_answers, flag = process_student_paper(PATH_PAPERS)
        evaluate(all_student_answers, marks, reference_answers, flag)
        # delete_dir(preprocessed)
        delete_dir(student_upload)
        pprint("Results are ready and stored in preprocessed!")

        zipf = zipfile.ZipFile(PATH_PAPERS + '/'+'Student_results.zip', 'w', )
        pprint('Zipping pdfs')
        for root, dirs, files in os.walk(PATH_PAPERS):
            for file in files:
                if file.endswith(".pdf"):
                    zipf.write(os.path.join(root, file),
                               basename(os.path.join(root, file)))
        zipf.close()
        pprint('Done')
        socketio.emit('text_response',
                      {'data': str('false')})
        resp.status_code = 200
        return resp


@app.route('/download')
def download_all():

    return send_file(PATH_PAPERS + '/'+'Student_results.zip',
                     mimetype='zip',
                     attachment_filename='Student_results.zip',
                     as_attachment=True)


if __name__ == '__main__':
    socketio.run(app, debug=False)
