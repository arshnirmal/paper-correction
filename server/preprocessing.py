#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:29:39 2020

@author: bhargavdesai
"""
import re
import os
import cv2
import numpy as np
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError)


# FILE_PATH = '/Users/bhargavdesai/Desktop/New Folder With Items'
# OUTPUT_PATH = '/Users/bhargavdesai/Desktop/Testing'
# os.mkdir(OUTPUT_PATH)

class image_preprocessing:
    def __init__(self, FILE_PATH, OUTPUT_PATH):
        self.FILE_PATH = FILE_PATH
        self.OUTPUT_PATH = OUTPUT_PATH

    def preprocess(self, PATH, idf):
        # TODO: Handle error if image is already processed
        try:
            for idx, img in enumerate(sorted(os.listdir(PATH))):

                img = cv2.imread(os.path.join(PATH, img), -1)
                print(img.shape)
                img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.bilateralFilter(img, 3, 75, 75)
                cv2.imwrite(os.path.join(
                    PATH, 'S'+str(idf)+'_'+str(idx)+'.png'), img)
            return None

        except NotADirectoryError:

            img = cv2.imread(PATH, -1)
            print(img.shape)
            img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(self.OUTPUT_PATH, 'PHOTOS',
                                     'S1'+'_'+str(idf)+'.png'), img)
            return None

    def flush_tempfiles(self, FLUSH_PATH):

        for file in os.listdir(FLUSH_PATH):
            if file.endswith('.ppm'):
                os.remove(os.path.join(FLUSH_PATH, file))
                
    def ensure_order(self, path):
        for img_file in os.listdir(path):
            num = img_file.split('-')[5]
            os.rename(os.path.join(path, img_file), os.path.join(path, num))

    def check_for_file_formats_and_process(self):
        FILE_PATH = self.FILE_PATH
        OUTPUT_PATH = self.OUTPUT_PATH

        pdf_count = 0
        images_count = 0
        others_count = 0
        others_file = []
        flag = None

        for file in sorted(os.listdir(FILE_PATH)):

            if file.endswith(('.jpg', '.jpeg', '.tif', '.png')):
                flag = 1
                images_count += 1
                if images_count == 1:
                    try:
                        os.mkdir(os.path.join(OUTPUT_PATH, 'PHOTOS'))
                    except:
                        pass

                self.preprocess(os.path.join(FILE_PATH, file), images_count)
                print(
                    'An image was found, processing and moving it in the directory "Photos" in the passed output path')

            elif file.endswith('.pdf'):
                flag = 2
                pdf_count += 1
                try:
                    os.mkdir(os.path.join(OUTPUT_PATH, 'S' + str(pdf_count)))
                except:
                    pass
                print('Found a PDF file')
                print('Created folder for Student ' + str(pdf_count))
                convert_from_path(os.path.join(FILE_PATH, file), output_folder=os.path.join(
                    OUTPUT_PATH, 'S'+str(pdf_count)+'/'))
                print('Converted scanned PDF to images for Student ' + str(pdf_count))
                print('Ensuring image files are tagged in order...')
                print('Preprocessing images for better OCR detection')
                print(os.path.join(OUTPUT_PATH, 'S'+str(pdf_count)+'/'))
                self.ensure_order(os.path.join(OUTPUT_PATH, 'S'+str(pdf_count)+'/'))
                self.preprocess(os.path.join(OUTPUT_PATH, 'S' +
                                             str(pdf_count)+'/'), pdf_count)
                print('Flushing uneccessary files.... Done!')
                self.flush_tempfiles(os.path.join(
                    OUTPUT_PATH, 'S'+str(pdf_count)+'/'))

            elif flag is None:
                print(not file.endswith(('.jpg', '.jpeg', '.tif', '.png', '.pdf')))
                others_count += 1
                others_file.append(file)
                if others_count != 0:
                    print(
                        'Found the following files with unrecognized extenstions, these files will not be evaluated:')
                    for i in len(others_file):
                        print(others_file[i])
                    print(
                        'For evaluation, please change the file to an image or a PDF document')

        return None
