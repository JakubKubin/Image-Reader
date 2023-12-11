from config import paths as path
from preprocess import preprocess as pp
from preprocess import imagemanager as im
import os
import time
import pytesseract

pytesseract.pytesseract.tesseract_cmd = path.TESSERACT_PATH

os.chdir(path.OUTPUT_PATH)

LANGUAGE = 'pol'
SAVE_PATH = path.OUTPUT_PATH

if __name__ == '__main__':
    startTime = time.process_time()

    image = im.get_image(path.IMAGE_PATH + r'\zdj.jpg')
    image_ROI = im.get_image(path.IMAGE_PATH + r'\zdj_ROI.jpg')
    image_TNR = im.get_image(path.IMAGE_PATH + r'\zdj_TNR.jpg')
    image_Calibri = im.get_image(path.IMAGE_PATH + r'\zdj_Calibri.jpg')
    image_Arial = im.get_image(path.IMAGE_PATH + r'\zdj_Arial.jpg')

    #im.image_to_text_file(image, LANGUAGE, SAVE_PATH, "original")
    #im.image_to_text_file(image_ROI, LANGUAGE, SAVE_PATH, "ROI")
    #im.image_to_text_file(image_TNR, LANGUAGE, SAVE_PATH, "TimesNewRoman")
    #im.image_to_text_file(image_Calibri, LANGUAGE, SAVE_PATH, "Calibri")
    #im.image_to_text_file(image_Arial, LANGUAGE, SAVE_PATH, "Arial")

    image_mean_masked = pp.mean_mask(image)
    im.image_to_text_file(image_mean_masked, LANGUAGE, SAVE_PATH, "mean_masked")
    im.save_image(SAVE_PATH + r'\out_original_mean.png', image_mean_masked)

    image_static_masked = pp.static_mask(image_Arial)
    im.image_to_text_file(image_static_masked, LANGUAGE, SAVE_PATH, "static_image_Arial")
    im.save_image(SAVE_PATH + r'\out_static_image_Arial.png', image_static_masked)

    image_gaussian_masked = pp.gaussian_mask(image_Arial)
    im.image_to_text_file(image_gaussian_masked, LANGUAGE, SAVE_PATH, "gaussian_masked_image_Arial")
    im.save_image(SAVE_PATH + r'\out_gaussian_masked_image_Arial.png', image_gaussian_masked)
    print("Time elapsed:", time.process_time() - startTime, "s")