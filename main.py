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
    image_Arial = im.get_image(path.IMAGE_PATH + r'\zdj_Arial.jpg')
    
    
    #skan +inne czcionki
    skan = im.get_image(path.IMAGE_PATH + r'\skan.jpg')
    skan_ROI = im.get_image(path.IMAGE_PATH + r'\skan_ROI.jpg')
    skan_Abadi = im.get_image(path.IMAGE_PATH + r'\skan_Abadi.jpg')
    skan_Ghotic = im.get_image(path.IMAGE_PATH + r'\skan_Ghotic.jpg')

    #im.image_to_text_file(image, LANGUAGE, SAVE_PATH, "original")
    #im.image_to_text_file(image_ROI, LANGUAGE, SAVE_PATH, "ROI")
    #im.image_to_text_file(image_TNR, LANGUAGE, SAVE_PATH, "TimesNewRoman")
    #im.image_to_text_file(image_Calibri, LANGUAGE, SAVE_PATH, "Calibri")
    #im.image_to_text_file(image_Arial, LANGUAGE, SAVE_PATH, "Arial")
    
    #im.image_to_text_file(skan, LANGUAGE, SAVE_PATH, "original_skan")
    #im.image_to_text_file(skan_ROI, LANGUAGE, SAVE_PATH, "skan_ROI")
    #im.image_to_text_file(skan_Abadi, LANGUAGE, SAVE_PATH, "Abadi")
    #im.image_to_text_file(skan_Ghotic, LANGUAGE, SAVE_PATH, "Ghotic")
    

    original_mean = apply_mask_and_save(image, pp.mean_mask, "mean_masked")
    original_static = apply_mask_and_save(image, pp.static_mask, "static_mask")
    
    #skan +inne czcionki
    skan_original_mean = apply_mask_and_save(skan, pp.mean_mask, "skan_mean_masked")
    skan_original_static = apply_mask_and_save(skan, pp.static_mask, "skan_static_mask")

    original_avg = pp.add_and_average(original_mean, original_static)
    apply_mask_and_save(original_avg, None, "avg_mean_static_original")
    
    #skan +inne czcionki
    skan_original_avg = pp.add_and_average(skan_original_mean, skan_original_static)
    apply_mask_and_save(skan_original_avg, None, "avg_mean_static_original_skan")
    
    
    
    #opened_original_mean = pp.open_binary_image(original_mean)
    opened_original_static = pp.open_binary_image(original_static)
    
    #skan +inne czcionki
    opened_original_static_skan = pp.open_binary_image(skan_original_static)

    original_avg_closed = pp.add_and_average(opened_original_static, original_mean)
    apply_mask_and_save(original_avg_closed, None, "avg_opened_mean_static_original")
    
    #skan +inne czcionki
    skan_original_avg_closed = pp.add_and_average(opened_original_static_skan, skan_original_mean)
    apply_mask_and_save(skan_original_avg_closed, None, "avg_opened_mean_static_original_skan")

    mean = apply_mask_and_save(image_Arial, pp.mean_mask, "mean_masked_Arial")
    static = apply_mask_and_save(image_Arial, pp.static_mask, "static_image_Arial")

    #skan +inne czcionki
    mean_skan = apply_mask_and_save(skan_Abadi, pp.mean_mask, "mean_masked_skan_Abadi")
    static_skan = apply_mask_and_save(skan_Abadi, pp.static_mask, "static_skan_Abadi")
    
    average = pp.add_and_average(mean, static)
    
    #skan +inne czcionki
    average_skan = pp.add_and_average(mean_skan, static_skan)

    apply_mask_and_save(average, None, "average_mean_static_image_Arial")
    #skan +inne czcionki
    apply_mask_and_save(average_skan, None, "average_mean_static_image_Abadi")

    print("Time elapsed:", time.process_time() - startTime, "s")