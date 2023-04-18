# Python OCR App

This is a Python application for Optical Character Recognition (OCR). It uses the Tesseract OCR engine to extract text from images in various file formats, including PDF, PNG, and JPG.

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Tesseract OCR installed on your system. If not, you can download it from the official Tesseract OCR website and install it.
3. Install the required Python libraries using the following command:

```
sh
pip install pytesseract opencv-python pdf2image
```

## Usage
1. Run the read_img.py file.
2. Provide the path to the image file you want to extract text from.
3. The program will automatically detect the file format (PDF, PNG, or JPG) and extract text from the image.
4. The extracted text will be printed on the console.
5. If the input file is a PDF, the program will convert each page of the PDF into separate PNG images and extract text from each page.
6. After extraction, the temporary PNG images will be deleted.

## Contributing
If you want to contribute to this Python OCR App, feel free to submit pull requests or open issues on the GitHub repository. Any contributions, feedback, or suggestions are welcome!

## License
This Python OCR App is open source and available under the MIT License.

## Credits
Tesseract OCR - Optical Character Recognition engine
OpenCV - Computer vision library for Python
pdf2image - Python library for converting PDFs to images
pytesseract - Python wrapper for Tesseract OCR engine

## Project Structure 
```
Project-Name
│   README.md
│   LICENSE
│   .gitignore
│   pom.xml
│
└───src
    ├───de
    │   ├───java
    │   │   └───com
    │   │       └───example
    │   │           ├───config
    │   │           ├───controller
    │   │           ├───model
    │   │           ├───repository
    │   │           └───service
    │   └───resources
    │       ├───static
    │       └───templates
    └───test
        └───java
            └───com
                └───example
                    ├───controller
                    ├───model
                    ├───repository
                    └───service
```
