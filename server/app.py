import io
import os
import requests
from pprint import pprint
from OCR import vision_ocr
from google.cloud import vision
from flask_cors import CORS
from google.cloud.vision import types
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, join_room, emit, send
from flask import Flask, jsonify, request, redirect, flash, url_for

app = Flask(__name__)

# Enble Cors
CORS(app)

socketio = SocketIO(app, cors_allowed_origins='*')

# setting GCP creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Paper Correction-59f4c4bd6353.json"
UPLOAD_FOLDER = os.getcwd() + '/img_data'
ALLOWED_EXTENSIONS = set(['png', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route('/test-server', methods=['GET'])
def test():
    text = request.args.get('user')
    return (jsonify({'text': text}))


@app.route('/file-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        print('no file')
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        print(resp)
        resp.status_code = 400
        return resp
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        resp = jsonify({'message': 'File successfully uploaded'})
        # TODO
        # myclass = vision_ocr('img_data/' + file.filename)
        # myobj = myclass.OCR()
        # text = myclass.parse_text(myobj)
        text = 'FILE UPLAODEED'
        pprint(text)
        socketio.emit('text_response',
                      {'data': str(text)})
        resp.status_code = 200
        return resp


if __name__ == '__main__':
    socketio.run(app, debug=True,)
