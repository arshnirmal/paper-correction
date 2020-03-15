import io
import os
import json
import argparse
import re
from enum import Enum
from pprint import pprint
from google.cloud import vision
from google.cloud.vision import types
from spellchecker import SpellChecker

# setting GCP creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Paper Correction-59f4c4bd6353.json"
misc_files = os.getcwd() + '/misc_files'


def spell_correction(text):
    correction = []
    spell = SpellChecker()
    spell.word_frequency.load_text_file(misc_files+'/correction_file.txt')
    word_list = list(text.split(" "))
    for word in word_list:
        correction.append(spell.correction(word))
    corr_text = ' '.join(correction)
    return corr_text


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


class processed_ocr:

    def __init__(self, flag):
        self.flag = flag

    def image_handle(self, ocr_path):
        for file in os.listdir(ocr_path):
            if not file.startswith('.'):
                print('Performing OCR on '+ocr_path + '/' + file)
                myclass = vision_ocr(ocr_path + '/' + file)
                myobj = myclass.OCR()
                text = myclass.parse_text(myobj)
                corrected_text = spell_correction(text)
                with open(ocr_path + '/results.txt', 'a+') as f:
                    f.writelines(corrected_text)
                os.remove(ocr_path + '/' + file)
        return print(f'Handled images at {ocr_path}')

    def pdf_handle(self, ocr_path):
        for folder in os.listdir(ocr_path):
            if (not folder.startswith('.')) and (folder != 'PHOTOS'):

                print('In folder ' + folder)
                for file in os.listdir(ocr_path + '/' + folder):
                    if not file.startswith('.'):
                        path = ocr_path + '/' + folder
                        print('Performing OCR on '+path + '/' + file)
                        myclass = vision_ocr(path + '/' + file)
                        myobj = myclass.OCR()
                        text = myclass.parse_text(myobj)
                        corrected_text = spell_correction(text)
                        with open(path + '/results.txt', 'a+') as f:
                            f.writelines(corrected_text)
                        os.remove(path + '/' + file)
                        print('removed ' + path + '/' + file)
        return print(f'Handled pdfs at {ocr_path}')

    def multiple_handler(self, ocr_path):
        for folder in os.listdir(ocr_path):
            if not folder.startswith('.'):
                if folder == 'PHOTOS':

                    self.image_handle(ocr_path+'/PHOTOS')
                elif re.match(r'S[0-9]', folder):
                    print("Looking for pdf files now in " + folder)
                    self.pdf_handle(ocr_path)
                else:
                    print('Unexpected file found, please check uploads')
        return print(f'Handled multiple files at {ocr_path}')
