# Recognizing text using the Tesseract library

## How to make things work:
- Use Python 3.9.12
- ```pip install --no-dependencies -r .\requirements.txt```
- Install Tesseract and Poppler

## How to install Tesseract OCR for Windows
- Download installer [Tesseract-OCR](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe)
- Install Tesseract for all users
- Select **ALL** components to be installed
- Use default destination folder - `C:\Program Files\Tesseract-OCR`

## How to install Poppler for Windows
- Download the latest poppler package from [@oschwartz10612](https://github.com/oschwartz10612/poppler-windows/releases/)
- Move the extracted directory to the desired place on your system
- Add the `bin/` directory to your PATH
- Test Poppler in **cmd** by running `pdftoppm -h`

## Throubleshooting
Possible issues are with incompatible packages, try using 'virtualenv' instead of default pip folder. Make sure that you use proper Python version.

## Pip list of working packages
- base256            1.0.1
- certifi            2022.12.7
- charset-normalizer 3.1.0
- click              8.1.3
- colorama           0.4.6
- emit               0.4.0
- Flask              2.2.3
- idna               3.4
- itsdangerous       2.1.2
- Jinja2             3.1.2
- MarkupSafe         2.1.2
- numpy              1.24.2
- opencv-python      4.8.1.78
- packaging          23.0
- pandas             1.5.3
- pdf2image          1.16.3
- Pillow             9.4.0
- pip                23.2.1
- prompt-toolkit     3.0.38
- pytesseract        0.3.10
- python-dateutil    2.8.2
- pytz               2022.7.1
- requests           2.28.2
- setuptools         67.1.0
- six                1.16.0
- urllib3            1.26.15
- wcwidth            0.2.6
- Werkzeug           2.2.3
- wheel              0.38.4