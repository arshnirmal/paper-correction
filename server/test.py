import io
import os
import requests
from pprint import pprint
from OCR import vision_ocr
from flask_cors import CORS
from google.cloud import vision
from google.cloud.vision import types
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, join_room, emit, send
from flask import Flask, jsonify, request, redirect
import logging
from flask_uploads import UploadSet, IMAGES


# initialize Flask
app = Flask(__name__)

socketio = SocketIO(app,cors_allowed_origins='*')



@socketio.on('connected_event')
def connected(msg):
    """WebSocket connect event
    This will trigger responsing a message to client
    """
    emit('server_response', {'data': msg['data']})



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Paper Correction-59f4c4bd6353.json"
UPLOAD_FOLDER = os.getcwd() + '/img_data'
ALLOWED_EXTENSIONS = set(['png', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/file-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    uploaded_files = request.files.getlist('file')
    print(uploaded_files)
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    text_file = uploaded_files[0]
    image_file= uploaded_files[1 ]
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        print(resp)
        resp.status_code = 4000
        return resp
    if file:
        filename = secure_filename(file.filename)
        # txt_filename = secure_filename(text.filename)

        print(os.path.join(UPLOAD_FOLDER, filename))
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        # text.save(os.path.join(UPLOAD_FOLDER, txt_filename))
        resp = jsonify({'message' : 'File successfully uploaded'})
        # myclass= vision_ocr('img_data/'+ file.filename)
        # myobj = myclass.OCR()
        # text = myclass.parse_text(myobj)
        # pprint(text)
        # socketio.emit('text_response',  {
        #           'data': str(text)}, broadcast=True)

        return resp




if __name__ == '__main__':
    socketio.run(app, debug=True,)
