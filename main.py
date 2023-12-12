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

def apply_mask_and_save(image, mask_function, output_filename, language='pol', save_path=SAVE_PATH):
    if mask_function is not None:
        masked_image = mask_function(image)
    else:
        masked_image = image
    im.image_to_text_file(masked_image, language, save_path, output_filename)
    im.save_image(save_path + fr'\out_{output_filename}.png', masked_image)
    return masked_image

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

    original_mean = apply_mask_and_save(image, pp.mean_mask, "mean_masked")
    original_static = apply_mask_and_save(image, pp.static_mask, "static_mask")

    original_avg = pp.add_and_average(original_mean, original_static)
    apply_mask_and_save(original_avg, None, "avg_mean_static_original")

    #opened_original_mean = pp.open_binary_image(original_mean)
    opened_original_static = pp.open_binary_image(original_static)

    original_avg_closed = pp.add_and_average(opened_original_static, original_mean)
    apply_mask_and_save(original_avg_closed, None, "avg_opened_mean_static_original")

    mean = apply_mask_and_save(image_Arial, pp.mean_mask, "mean_masked_Arial")
    static = apply_mask_and_save(image_Arial, pp.static_mask, "static_image_Arial")

    average = pp.add_and_average(mean, static)

    apply_mask_and_save(average, None, "average_mean_static_image_Arial")

    print("Time elapsed:", time.process_time() - startTime, "s")