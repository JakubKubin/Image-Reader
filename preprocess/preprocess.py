import cv2
import numpy as np

def image_to_gray_scale(image):
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def mean_mask(image):
    return cv2.adaptiveThreshold(image_to_gray_scale(image), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

def static_mask(image):
    lower_mask_value = np.array([100, 100, 100])
    upper_mask_value = np.array([255, 255, 255])
    return cv2.inRange(image, lower_mask_value, upper_mask_value)

def gaussian_mask(image):
    return cv2.adaptiveThreshold(image_to_gray_scale(image), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
