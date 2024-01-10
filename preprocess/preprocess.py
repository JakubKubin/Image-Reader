import cv2
import numpy as np

def image_to_gray_scale(image):
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def mean_mask(image):
    return cv2.adaptiveThreshold(image_to_gray_scale(image), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 11)

def static_mask(image):
    lower_mask_value = np.array([100, 100, 100])
    upper_mask_value = np.array([255, 255, 255])
    return cv2.inRange(image, lower_mask_value, upper_mask_value)

def gaussian_mask(image):
    return cv2.adaptiveThreshold(image_to_gray_scale(image), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

def add_and_average(first_image, second_image):
    if first_image.shape == second_image.shape:
        return cv2.add(np.uint8(first_image), np.uint8(second_image)) // 2

def open_binary_image(image):
    eroded_horizontal = cv2.erode(np.uint8(image), np.ones((4, 4), np.uint8), iterations=1)
    return cv2.dilate(eroded_horizontal, np.ones((1, 1), np.uint8))

def close_binary_image(image):
    dilated_horizontal = cv2.dilate(np.uint8(image), np.ones((3, 3), np.uint8), iterations=1)
    return cv2.erode(dilated_horizontal, np.ones((2, 2), np.uint8))

def image_to_binary(image):
    if len(image.shape) != 2:
        raise ValueError("Invalid input: 'image' must be a grayscale image (1 channel) for thresholding.")
    _, binary_image = cv2.threshold(np.uint8(image), 0, 255, cv2.THRESH_BINARY)
    return binary_image

def otsu_mask(image):
    try:
        image = image_to_gray_scale(image)

        # Calculate normalized histogram and its cumulative distribution function
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_norm = hist.ravel() / hist.sum()
        cumulative_distribution = hist_norm.cumsum()

        # Iterate through possible thresholds to find the optimal one using Otsu's method
        fn_min = np.inf
        optimal_thresh = -1

        for i in range(1, 256):
            p1, p2 = np.hsplit(hist_norm, [i])  # Probabilities
            q1, q2 = cumulative_distribution[i], cumulative_distribution[255] - cumulative_distribution[i]

            if q1 < 1.e-6 or q2 < 1.e-6:
                continue

            b1, b2 = np.hsplit(np.arange(256), [i])  # Weights

            # Calculate means and variances
            m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
            v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

            # Calculate the minimization function
            fn = v1 * q1 + v2 * q2

            if fn < fn_min:
                fn_min = fn
                optimal_thresh = i

        # Apply the optimal threshold to get the binary image
        _, otsu = cv2.threshold(image, optimal_thresh, 255, cv2.THRESH_BINARY)
        return otsu
    except Exception as error:
        raise Exception(f"Error while applying Otsu's thresholding:\nError: {str(error)}")