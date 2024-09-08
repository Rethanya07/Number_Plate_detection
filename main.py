import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

states = {
    'AN': 'Andaman and Nicobar Islands', 'AP': 'Andhra Pradesh', 'AR': 'Arunachal Pradesh', 'AS': 'Assam',
    'BR': 'Bihar', 'CH': 'Chandigarh', 'CT': 'Chhattisgarh', 'DN': 'Dadra and Nagar Haveli', 'DD': 'Daman and Diu',
    'DL': 'Delhi', 'GA': 'Goa', 'GJ': 'Gujarat', 'HR': 'Haryana', 'HP': 'Himachal Pradesh', 'JK': 'Jammu and Kashmir',
    'JH': 'Jharkhand', 'KA': 'Karnataka', 'KL': 'Kerala', 'LD': 'Lakshadweep', 'MP': 'Madhya Pradesh', 'MH': 'Maharashtra',
    'MN': 'Manipur', 'ML': 'Meghalaya', 'MZ': 'Mizoram', 'NL': 'Nagaland', 'OD': 'Odisha', 'PB': 'Punjab',
    'PY': 'Puducherry', 'RJ': 'Rajasthan', 'SK': 'Sikkim', 'TN': 'Tamil Nadu', 'TS': 'Telangana', 'TR': 'Tripura',
    'UP': 'Uttar Pradesh', 'UK': 'Uttarakhand', 'WB': 'West Bengal'
}

def extract_num(img_name):
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in nplate:
        a, b = (int(0.02 * img.shape[0]), int(0.025 * img.shape[1]))
        plate = img[y + a:y + h - a, x + b:x + w - b, :]

        # Preprocessing
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        plate_blur = cv2.GaussianBlur(plate_gray, (5, 5), 0)
        _, plate_thresh = cv2.threshold(plate_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # OCR with additional configurations
        custom_config = r'--oem 3 --psm 6'
        read = pytesseract.image_to_string(plate_thresh, config=custom_config)
        read = ''.join(e for e in read if e.isalnum()).upper()

        stat = read[0:2].strip().upper()

        try:
            print(f'Car Belongs to {states[stat]} - Number Plate: {read}')
        except KeyError:
            print('State not recognised!!')

        cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)
        cv2.rectangle(img, (x, y - 40), (x + w, y), (51, 51, 255), 2)
        cv2.putText(img, read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (51, 51, 255), 2)
        cv2.imshow('plate',plate_thresh)

    cv2.imshow("Result", img)
    cv2.imwrite('image.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

extract_num('car7.jpg')
