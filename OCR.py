import os
import io
import re
import cv2
import json
import argparse
import numpy as np
from pprint import pprint
from google.cloud import vision
from google.cloud.vision_v1 import types
from spellchecker import SpellChecker
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError

# Setting GCP creds
credential_path = "/mnt/data/Arsh/Computer Science/Python/paper-correction/secret_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
misc_files = os.getcwd() + '/misc_files'


def spell_correction(text):
    correction = []
    spell = SpellChecker()
    spell.word_frequency.load_text_file(misc_files+'/correction_file.txt')
    word_list = text.split(" ")
    for word in word_list:
        corrected_word = spell.correction(word)
        correction.append(corrected_word if corrected_word is not None else word)
    corr_text = ' '.join(correction)
    return corr_text


class VisionOCR:
    def __init__(self, img_file):
        self.img = str(img_file)

    def ocr(self):
        client = vision.ImageAnnotatorClient()
        with io.open(self.img, 'rb') as imagefile:
            content = imagefile.read()
        image = types.Image(content=content)
        response = client.document_text_detection(image=image)
        return response

    def parse_text(self, response):
        return response.full_text_annotation.text


class ProcessedOCR:
    def __init__(self, flag):
        self.flag = flag

    def handle_image(self, ocr_path):
        for file in sorted(os.listdir(ocr_path)):
            if not file.startswith('.'):
                print(f'Performing OCR on {ocr_path}/{file}')
                ocr_class = VisionOCR(f'{ocr_path}/{file}')
                ocr_result = ocr_class.ocr()
                text = ocr_class.parse_text(ocr_result)
                corrected_text = spell_correction(text)
                with open(f'{ocr_path}/results.txt', 'a+') as f:
                    f.write(corrected_text)
                os.remove(f'{ocr_path}/{file}')
        print(f'Handled images at {ocr_path}')

    def handle_pdf(self, ocr_path):
        for folder in sorted(os.listdir(ocr_path)):
            if not folder.startswith('.') and folder != 'PHOTOS':
                print(f'In folder {folder}')
                folder_path = f'{ocr_path}/{folder}'
                for file in sorted(os.listdir(folder_path)):
                    if not file.startswith('.'):
                        print(f'Performing OCR on {folder_path}/{file}')
                        ocr_class = VisionOCR(f'{folder_path}/{file}')
                        ocr_result = ocr_class.ocr()
                        text = ocr_class.parse_text(ocr_result)
                        corrected_text = spell_correction(text)
                        with open(f'{folder_path}/results.txt', 'a+') as f:
                            f.write(corrected_text)
                        os.remove(f'{folder_path}/{file}')
                        print(f'Removed {folder_path}/{file}')
        print(f'Handled PDFs at {ocr_path}')

    def handle_multiple(self, ocr_path):
        for folder in os.listdir(ocr_path):
            if not folder.startswith('.'):
                if folder == 'PHOTOS':
                    self.handle_image(f'{ocr_path}/PHOTOS')
                elif re.match(r'S[0-9]', folder):
                    print(f"Looking for PDF files now in {folder}")
                    self.handle_pdf(ocr_path)
                else:
                    print('Unexpected file found, please check uploads')
        print(f'Handled multiple files at {ocr_path}')


class ImagePreprocessing:
    def __init__(self, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path

    def preprocess(self, path, idf):
        try:
            if os.path.isdir(path):
                for idx, img_name in enumerate(sorted(os.listdir(path))):
                    img_path = os.path.join(path, img_name)
                    img = cv2.imread(img_path, -1)
                    if img is None:
                        print(f"Error reading image {img_path}")
                        continue
                    img = self.process_image(img)
                    output_file = os.path.join(path, f'S{idf}_{idx}.png')
                    cv2.imwrite(output_file, img)
            else:
                img = cv2.imread(path, -1)
                if img is None:
                    print(f"Error reading image {path}")
                    return
                img = self.process_image(img)
                photos_dir = os.path.join(self.output_path, 'PHOTOS')
                os.makedirs(photos_dir, exist_ok=True)
                output_file = os.path.join(photos_dir, f'S1_{idf}.png')
                cv2.imwrite(output_file, img)
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")

    def process_image(self, img):
        # Check the number of channels in the image
        if img.ndim == 2:
            # Convert grayscale to BGR
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif img.shape[2] == 1:
            # Convert single channel to BGR
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif img.shape[2] == 4:
            # Convert BGRA to BGR
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Now img should be in BGR format
        img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bilateralFilter(img, 3, 75, 75)
        return img

    def flush_tempfiles(self, flush_path):
        for file in os.listdir(flush_path):
            if file.endswith('.ppm'):
                os.remove(os.path.join(flush_path, file))

    def ensure_order(self, path):
        for img_file in os.listdir(path):
            print(f'Renaming {img_file} in {path}')
            num = img_file.split('-')[-1]
            os.rename(os.path.join(path, img_file), os.path.join(path, num))

    def check_and_process_files(self):
        pdf_count = 0
        images_count = 0
        other_files = []

        for file in sorted(os.listdir(self.file_path)):
            file_path = os.path.join(self.file_path, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.tif', '.png')):
                images_count += 1
                self._process_image_file(file_path, images_count)
            elif file.lower().endswith('.pdf'):
                pdf_count += 1
                self._process_pdf_file(file_path, pdf_count)
            else:
                other_files.append(file)

        if other_files:
            print('Found the following files with unrecognized extensions:')
            for file in other_files:
                print(file)
            print('These files will not be evaluated. Please use images or PDF documents.')

    def _process_image_file(self, file_path, images_count):
        try:
            self.preprocess(file_path, images_count)
            print('An image was found, processing and moving it to the "PHOTOS" directory in the output path.')
        except Exception as e:
            print(f"Error processing image file {file_path}: {e}")

    def _process_pdf_file(self, file_path, pdf_count):
        try:
            student_dir = os.path.join(self.output_path, f'S{pdf_count}')
            os.makedirs(student_dir, exist_ok=True)
            print(f'Found a PDF file. Created folder for Student {pdf_count}')
            convert_from_path(file_path, output_folder=student_dir)
            print(f'Converted scanned PDF to images for Student {pdf_count}')
            self.ensure_order(student_dir)
            print('Preprocessing images for better OCR detection...')
            self.preprocess(student_dir, pdf_count)
            print('Flushing unnecessary files... Done!')
            self.flush_tempfiles(student_dir)
        except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
            print(f"Error processing PDF file {file_path}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Usage example:
# FILE_PATH = '/path/to/your/input/files'
# OUTPUT_PATH = '/path/to/your/output/files'
# os.makedirs(OUTPUT_PATH, exist_ok=True)
# img_proc = ImagePreprocessing(FILE_PATH, OUTPUT_PATH)
# img_proc.check_and_process_files()
