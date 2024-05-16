import io
import os
import re
import zipfile
import requests
import sys
import shutil
import logging
from pathlib import Path
from pprint import pprint
from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS
from flask_socketio import SocketIO
from google.cloud import vision
from spellchecker import SpellChecker
from werkzeug.utils import secure_filename
from OCR import VisionOCR, ProcessedOCR
from preprocessing import ImagePreprocessing
from report import process_answer_key, process_student_paper, evaluate

# Initialize Flask app
app = Flask(__name__, template_folder="templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Enable CORS
CORS(app)

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins='*')

# Set up logging
logging.getLogger('socketio').disabled = True
logging.getLogger('engineio').disabled = True

# Set Google Cloud credentials
credential_path = "/mnt/data/Arsh/Computer Science/Python/paper-correction/secret_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# Directory paths
student_upload = os.path.join(os.getcwd(), 'student_files')
misc_files = os.path.join(os.getcwd(), 'misc_files')
preprocessed = os.path.join(os.getcwd(), 'preprocessed')
PATH_ANSKEY = os.path.join(misc_files, 'master_file.txt')
PATH_PAPERS = preprocessed

# Ensure required directories exist
Path(student_upload).mkdir(parents=True, exist_ok=True)
Path(misc_files).mkdir(parents=True, exist_ok=True)
Path(preprocessed).mkdir(parents=True, exist_ok=True)

# Helper function to delete .DS_Store files


def dstore_delete():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file == '.DS_Store':
                os.remove(os.path.join(root, file))


dstore_delete()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/test', methods=['GET'])
def test():
    socketio.emit('text_response', {'data': str('false')})
    return '', 204


def spell_correction(text):
    spell = SpellChecker()
    spell.word_frequency.load_text_file(
        os.path.join(misc_files, 'correction_file.txt'))
    correction = [spell.correction(word) if spell.correction(
        word) else word for word in text.split()]
    return ' '.join(correction)


@app.route('/student-upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    files = request.files.getlist('file')
    if not files:
        return jsonify({'message': 'No files provided'}), 400

    for file in files:
        filename = secure_filename(file.filename)
        ext = filename.split('.')[-1]
        file_name = f'student_{files.index(file)}.{ext}'
        file.save(os.path.join(student_upload, file_name))

    return jsonify({'message': 'File(s) successfully uploaded'}), 200


@app.route('/master-upload', methods=['POST'])
def master_file():
    if 'master' not in request.files and 'correction' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    master_file = request.files.get('master')
    if master_file:
        master_filename = secure_filename(master_file.filename)
        master_name = f'master_file.{master_filename.split(".")[-1]}'
        master_file.save(os.path.join(misc_files, master_name))

    return jsonify({'message': 'File successfully uploaded'}), 200


@app.route('/correct-upload', methods=['POST'])
def correct_file():
    if 'correction' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    autocorrect = request.files.get('correction')
    if autocorrect:
        correction_filename = secure_filename(autocorrect.filename)
        correction_name = f'correction_file.{correction_filename.split(".")[-1]}'
        if correction_name.split('.')[-1] != 'txt':
            return jsonify({'message': 'File format not supported, please upload a .txt file'}), 400
        autocorrect.save(os.path.join(misc_files, correction_name))

        preprocessor = ImagePreprocessing(student_upload, preprocessed)
        preprocessor.check_and_process_files()

        dir_flag = None
        if os.path.isdir(os.path.join(preprocessed, "S1")) and os.path.isdir(os.path.join(preprocessed, "PHOTOS")):
            ocr_path, dir_flag = preprocessed, 'multiple'
        elif os.path.isdir(os.path.join(preprocessed, "PHOTOS")):
            ocr_path, dir_flag = os.path.join(
                preprocessed, "PHOTOS"), 'photo'
        elif os.path.isdir(os.path.join(preprocessed, "S1")):
            ocr_path, dir_flag = preprocessed, 'pdf'

        if dir_flag:
            handler = ProcessedOCR(dir_flag)
            if dir_flag == 'photo':
                handler.handle_image(ocr_path)
            elif dir_flag == 'pdf':
                handler.handle_pdf(ocr_path)
            elif dir_flag == 'multiple':
                handler.handle_multiple(ocr_path)
        else:
            return jsonify({'message': 'Error processing files, please restart'}), 500

        dstore_delete()

        marks, reference_answers = process_answer_key(PATH_ANSKEY)
        all_student_answers, flag = process_student_paper(PATH_PAPERS)
        evaluate(all_student_answers, marks, reference_answers, flag)

        shutil.rmtree(student_upload)
        pprint("Results are ready and stored in preprocessed!")

        with zipfile.ZipFile(os.path.join(PATH_PAPERS, 'Student_results.zip'), 'w') as zipf:
            for root, dirs, files in os.walk(PATH_PAPERS):
                for file in files:
                    if file.endswith(".pdf"):
                        zipf.write(os.path.join(root, file),
                                   os.path.basename(os.path.join(root, file)))

        socketio.emit('text_response', {'data': str('false')})
        return jsonify({'message': 'Files processed and results prepared'}), 200


@app.route('/download')
def download_all():
    return send_file(os.path.join(PATH_PAPERS, 'Student_results.zip'), mimetype='zip', attachment_filename='Student_results.zip', as_attachment=True)


if __name__ == '__main__':
    socketio.run(app, debug=False)
