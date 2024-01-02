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

    #image = im.get_image(path.IMAGE_PATH + r'\zdj.jpg')
    image_ROI = im.get_image(path.IMAGE_PATH + r'\zdj_ROI.jpg')
    skan_Abadi = im.get_image(path.IMAGE_PATH + r'\skan_Abadi.jpg')
    skan_Ghotic = im.get_image(path.IMAGE_PATH + r'\skan_Ghotic.jpg')
    #image_TNR = im.get_image(path.IMAGE_PATH + r'\zdj_TNR.jpg')
    #image_Calibri = im.get_image(path.IMAGE_PATH + r'\zdj_Calibri.jpg')
    #image_Arial = im.get_image(path.IMAGE_PATH + r'\zdj_Arial.jpg')

    #im.image_to_text_file(image, LANGUAGE, SAVE_PATH, "original")
    #im.image_to_text_file(image_ROI, LANGUAGE, SAVE_PATH, "ROI")
    #im.image_to_text_file(image_TNR, LANGUAGE, SAVE_PATH, "TimesNewRoman")
    #im.image_to_text_file(image_Calibri, LANGUAGE, SAVE_PATH, "Calibri")
    #im.image_to_text_file(image_Arial, LANGUAGE, SAVE_PATH, "Arial")

    #im.image_to_text_file(skan, LANGUAGE, SAVE_PATH, "original_skan")
    #im.image_to_text_file(skan_ROI, LANGUAGE, SAVE_PATH, "skan_ROI")
    im.image_to_text_file(skan_Abadi, LANGUAGE, SAVE_PATH, "skan_Abadi")
    im.image_to_text_file(skan_Ghotic, LANGUAGE, SAVE_PATH, "skan_Ghotic")

    roi_mean = apply_mask_and_save(image_ROI, pp.mean_mask, "mean_masked_ROI")
    roi_otsu = apply_mask_and_save(image_ROI, pp.otsu_mask, "otsu_masked_ROI")

    roi_mean_closed = apply_mask_and_save(roi_mean, pp.close_binary_image, "closed_mean_masked_ROI")
    avg_roi_mean_closed_otsu = pp.add_and_average(roi_mean_closed, roi_otsu)
    binary_avg_roi_mean_closed_otsu = apply_mask_and_save(avg_roi_mean_closed_otsu, pp.image_to_binary, "avg_closed_mean_otsu_ROI")
    open_binary_avg_roi_mean_closed_otsu = apply_mask_and_save(binary_avg_roi_mean_closed_otsu, pp.open_binary_image, "binary_avg_roi_mean_closed_otsu_ROI")

    print("Time elapsed:", time.process_time() - startTime, "s")