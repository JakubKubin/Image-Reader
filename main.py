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
    im.image_to_text_file(masked_image, language, save_path+r'\texts', output_filename)
    im.save_image(save_path+r'\images' + fr'\out_{output_filename}.png', masked_image)
    return masked_image

if __name__ == '__main__':
    startTime = time.process_time()

    #zdjecie z podstawowymi czcionkami
    image = im.get_image(path.IMAGE_PATH + r'\zdj.jpg')
    image_ROI = im.get_image(path.IMAGE_PATH + r'\zdj_ROI.jpg')
    image_TNR = im.get_image(path.IMAGE_PATH + r'\zdj_TNR.jpg')
    image_Calibri = im.get_image(path.IMAGE_PATH + r'\zdj_Calibri.jpg')
    image_Arial = im.get_image(path.IMAGE_PATH + r'\zdj_Arial.jpg')

    #apply_mask_and_save(image, None, "zdj_original")
    #apply_mask_and_save(image_ROI, None, "zdj_ROI")
    apply_mask_and_save(image_TNR, None, "zdj_TimesNewRoman")
    apply_mask_and_save(image_Calibri, None, "zdj_Calibri")
    apply_mask_and_save(image_Arial, None, "zdj_Arial")

    #skan z podstawowymi czcionkami
    '''
    skan_podst = im.get_image(path.IMAGE_PATH + r'\skan_podst.jpg')
    skan_podst_ROI = im.get_image(path.IMAGE_PATH + r'\skan_podst_ROI.jpg')
    skan_podst_TNR = im.get_image(path.IMAGE_PATH + r'\skan_podst_TNR.jpg')
    skan_podst_Calibri = im.get_image(path.IMAGE_PATH + r'\skan_podst_Calibri.jpg')
    skan_podst_Arial = im.get_image(path.IMAGE_PATH + r'\skan_podst_Arial.jpg')

    apply_mask_and_save(skan_podst, None, "skan_podst")
    apply_mask_and_save(skan_podst_ROI, None, "skan_podst_ROI")
    apply_mask_and_save(skan_podst_TNR, None, "skan_podst_TNR")
    apply_mask_and_save(skan_podst_Calibri, None, "skan_podst_Calibri")
    apply_mask_and_save(skan_podst_Arial, None, "skan_podst_Arial")
    '''

    #skan z innymi czcionkami
    '''
    skan = im.get_image(path.IMAGE_PATH + r'\skan.jpg')
    skan_ROI = im.get_image(path.IMAGE_PATH + r'\skan_ROI.jpg')
    skan_Abadi = im.get_image(path.IMAGE_PATH + r'\skan_Abadi.jpg')
    skan_Ghotic = im.get_image(path.IMAGE_PATH + r'\skan_Ghotic.jpg')

    apply_mask_and_save(skan, None, "skan_inne_czcionki")
    apply_mask_and_save(skan_ROI, None, "skan_inne_czcionki_ROI")
    apply_mask_and_save(skan_Abadi, None, "skan_inne_czcionki_Abadi")
    apply_mask_and_save(skan_Ghotic, None, "skan_inne_czcionki_Ghotic")

    '''
    #przetwarzanie zdjecia
    '''
    original_mean = apply_mask_and_save(image, pp.mean_mask, "mean_masked")
    original_otsu = apply_mask_and_save(image, pp.otsu_mask, "otsu_mask")

    original_avg = pp.add_and_average(original_mean, original_otsu)
    apply_mask_and_save(original_avg, pp.image_to_binary, "avg_mean_otsu_original")

    opened_original_otsu = pp.open_binary_image(original_otsu)

    opened_avg_original_otsu = pp.add_and_average(opened_original_otsu, original_mean)
    apply_mask_and_save(opened_avg_original_otsu, pp.image_to_binary, "avg_opened_mean_otsu_original")

    #zdjecie z podstawowymi czcionkami
    mean = apply_mask_and_save(image_Arial, pp.mean_mask, "mean_masked_Arial")
    otsu = apply_mask_and_save(image_Arial, pp.otsu_mask, "otsu_masked_Arial")

    average = pp.add_and_average(mean, otsu)

    apply_mask_and_save(average, pp.image_to_binary, "avg_mean_otsu_image_Arial")
    '''
    Arial_mean = apply_mask_and_save(image_Arial, pp.mean_mask, "Arial_mean_masked")
    Arial_otsu = apply_mask_and_save(image_Arial, pp.otsu_mask, "Arial_otsu_mask")

    original_avg = pp.add_and_average(Arial_mean, Arial_otsu)
    apply_mask_and_save(original_avg, pp.image_to_binary, "avg_mean_otsu_Arial")

    opened_Arial_otsu = pp.open_binary_image(Arial_otsu)

    opened_avg_original_otsu = pp.add_and_average(opened_Arial_otsu, Arial_mean)
    apply_mask_and_save(opened_avg_original_otsu, pp.image_to_binary, "avg_opened_mean_otsu_Arial")

    print("Time elapsed:", time.process_time() - startTime, "s")