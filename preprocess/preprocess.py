import cv2

def image_to_gray_scale(image):
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def mean_mask(image):
    return cv2.adaptiveThreshold(image_to_gray_scale(image), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
