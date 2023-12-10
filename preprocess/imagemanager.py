import cv2
import pytesseract
import numpy as np
import os

SUPPORTED_LANGUAGES = pytesseract.get_languages()
SUPPORTED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

def show_image(image):
    try:
        if not isinstance(image, np.ndarray):
            raise ValueError("Invalid image data provided.")

        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
    except Exception as error:
        raise Exception(f'Error while displaying the image:\n{str(error)}')

def get_image(image_path):
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file does not exist: {image_path}")
        if not image_path.lower().endswith(tuple(SUPPORTED_IMAGE_EXTENSIONS)):
            raise ValueError(f"Unsupported image format: {image_path}")
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Failed to load the image: {image_path}")
        return image
    except Exception as error:
        raise ValueError(f"Error while trying to load the image: {str(error)}")

def save_image(file_path, image):
    try:
        if not file_path:
            raise ValueError("File path is empty.")
        if not isinstance(image, np.ndarray):
            raise ValueError("Invalid image data provided.")
        if not cv2.imwrite(file_path, image):
            raise ValueError(f"Failed to save image to: {file_path}")
    except Exception as error:
        raise ValueError(f"Error while trying to save image to: {file_path}\nError: {str(error)}")

def image_to_text(image, language):
    try:
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language for OCR: {language}")
        return pytesseract.image_to_string(image, lang=language)
    except Exception as error:
        raise Exception(f'Error while using Tesseract:\nError: {str(error)}')

def image_to_text_file(image, language, save_path, save_filename):
    try:
        if not isinstance(image, np.ndarray):
            raise ValueError("Invalid image data provided.")
        if not os.path.exists(save_path):
            raise FileNotFoundError(f"Save directory does not exist: {save_path}")

        text = image_to_text(image, language)

        with open(f'{save_path}\{save_filename}.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'File saved at {save_path}\{save_filename}.txt')

    except Exception as error:
        raise Exception(f'Error while saving image to text file:\n{str(error)}')