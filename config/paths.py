import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_PATH = BASE_DIR + r'\output'

IMAGE_PATH = BASE_DIR + r'\images'

TESSERACT_PATH = r'C:/Program Files/Tesseract-OCR/tesseract.exe' #default tesseract path on windows

TESSERACT_PATH_MAC = r'/opt/homebrew/Cellar/tesseract/5.3.0_1/bin/tesseract' #default tesseract path on macOS (requires homebrew)