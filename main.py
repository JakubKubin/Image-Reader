from config import paths as path
from preprocess import imagemanager as im
import os
import time
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = path.TESSERACT_PATH

os.chdir(path.OUTPUT_PATH)

LANGUAGE = 'pol'
PATH_TO_IMAGE = path.IMAGE_PATH + r'\z1.png'
SAVE_PATH = path.OUTPUT_PATH + r'\tekst.txt'

if __name__ == '__main__':
    startTime = time.process_time()

    image = im.get_image(PATH_TO_IMAGE)
    text = im.image_to_text(image, LANGUAGE)
    print(text)

    try:
        with open(SAVE_PATH, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f'File saved at {SAVE_PATH}\n')
    except Exception as e:
        print(f'Error while saving image to text file:\n{str(e)}')

    print("Time elapsed:", time.process_time() - startTime, "s")