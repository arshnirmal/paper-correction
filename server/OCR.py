import io
import os
import json
import argparse
from enum import Enum
from pprint import pprint
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ExifTags

# setting GCP creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Paper Correction-59f4c4bd6353.json"


class vision_ocr:
    def __init__(self, img_file):
        self.img = str(img_file)

    def OCR(self):
        img = self.img
        client = vision.ImageAnnotatorClient()
        with io.open(img, 'rb') as imagefile:
            content = imagefile.read()
        image = types.Image(content=content)
        response = client.document_text_detection(image=image)
        return response

    def parse_text(self, response):
        text = response.full_text_annotation.text
        return text

