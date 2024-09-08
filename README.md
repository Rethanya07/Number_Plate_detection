# Number_Plate_detection
Number Plate Detection using OpenCV and Tesseract

DESCRIPTION

This project is a Python-based number plate detection system that uses OpenCV for image processing and Tesseract OCR for extracting text from the detected number plates. It detects vehicle number plates from images and identifies the state of registration based on the first two characters of the license plate.

KEY FEATURES:

-Detects number plates from car images using OpenCV and Haar cascades.

-Uses Tesseract OCR to extract text from detected plates.

-Identifies the state of vehicle registration in India based on the number plate prefix.

-Can be used for applications such as automated toll collection, traffic monitoring, and vehicle tracking.

TABLE OF CONTENTS

 1.Installation
 
 2.Usage
 
 3.Supported States
 
 4.Project Structure
 
 5.Technologies Used
 
 6.License
 
INSTALLATION

1.Prerequisites:

Before you begin, ensure you have the following installed:

 Python 3.x
 
 OpenCV
 
 Tesseract OCR
 
 Numpy
 
You can install the necessary libraries using pip:

pip install opencv-python pytesseract numpy

2.Tesseract Installation:

Download and install Tesseract from here.

Once installed, make sure to add the Tesseract executable path to your system's environment variables.

3.Clone the Repository

git clone https://github.com/your-username/number-plate-detection.git

cd number-plate-detection

4.Usage

Place your test images in the project folder.
Update the path to the Haarcascade classifier file and Tesseract executable in the script (no_plate.py).

5.Run the script:

python no_plate.py
The detected number plate and its associated state will be displayed on the screen.


PROJECT STRUCTURE

number-plate-detection/

│

├── haarcascade_russian_plate_number.xml    # Haarcascade file for detecting number plates

├── no_plate.py                             # Main Python script for detecting and reading number plates

├── README.md                               # Project documentation

└── test_images/                            # Directory for test images

TECHNOLOGIES USED

Python: The primary programming language used.

OpenCV: Used for image processing and number plate detection.

Tesseract OCR: Used for text extraction from the detected number plate.

NumPy: Used for matrix operations and image manipulations.

LICENSE

This project is licensed under the MIT License. See the LICENSE file for more details.
