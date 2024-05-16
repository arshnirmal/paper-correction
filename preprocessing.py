import os
import cv2
import numpy as np
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError


class ImagePreprocessing:
    def __init__(self, file_path, output_path):
        """
        Initializes the ImagePreprocessing class with input and output paths.
        """
        self.file_path = file_path
        self.output_path = output_path

    def preprocess_image(self, path, identifier):
        """
        Preprocesses the image or images in the specified path.
        """
        try:
            if os.path.isdir(path):
                for idx, img_name in enumerate(sorted(os.listdir(path))):
                    img_path = os.path.join(path, img_name)
                    img = cv2.imread(img_path, -1)
                    if img is None:
                        print(f"Error reading image {img_path}")
                        continue
                    img = self.process_image(img)
                    output_file = os.path.join(
                        path, f'S{identifier}_{idx}.png')
                    cv2.imwrite(output_file, img)
            else:
                img = cv2.imread(path, -1)
                if img is None:
                    print(f"Error reading image {path}")
                    return
                img = self.process_image(img)
                photos_dir = os.path.join(self.output_path, 'PHOTOS')
                os.makedirs(photos_dir, exist_ok=True)
                output_file = os.path.join(photos_dir, f'S1_{identifier}.png')
                cv2.imwrite(output_file, img)
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")

    def process_image(self, img):
        """
        Applies preprocessing steps to the image for better OCR detection.
        """
        img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bilateralFilter(img, 3, 75, 75)
        return img

    def flush_tempfiles(self, flush_path):
        """
        Removes temporary files from the specified directory.
        """
        for file in os.listdir(flush_path):
            if file.endswith('.ppm'):
                os.remove(os.path.join(flush_path, file))

    def ensure_order(self, path):
        """
        Ensures that the image files are named in sequential order.
        """
        for img_file in os.listdir(path):
            print(f'Renaming {img_file} in {path}')
            num = img_file.split('-')[-1]
            os.rename(os.path.join(path, img_file), os.path.join(path, num))

    def check_and_process_files(self):
        """
        Checks the input directory for image and PDF files and processes them.
        """
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
            print(
                'These files will not be evaluated. Please use images or PDF documents.')

    def _process_image_file(self, file_path, images_count):
        """
        Processes an individual image file.
        """
        try:
            self.preprocess_image(file_path, images_count)
            print(
                'An image was found, processing and moving it to the "PHOTOS" directory in the output path.')
        except Exception as e:
            print(f"Error processing image file {file_path}: {e}")

    def _process_pdf_file(self, file_path, pdf_count):
        """
        Processes an individual PDF file.
        """
        try:
            student_dir = os.path.join(self.output_path, f'S{pdf_count}')
            os.makedirs(student_dir, exist_ok=True)
            print(f'Found a PDF file. Created folder for Student {pdf_count}')
            convert_from_path(file_path, output_folder=student_dir)
            print(f'Converted scanned PDF to images for Student {pdf_count}')
            self.ensure_order(student_dir)
            print('Preprocessing images for better OCR detection...')
            self.preprocess_image(student_dir, pdf_count)
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
