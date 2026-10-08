import cv2
import numpy as np
from exeptions import *
from pathlib import Path
from enums import Format


def load_image(file_path: str) -> cv2.Mat:
    img = cv2.imread(file_path)
    file_format = Path(file_path).suffix
    if file_format != Format.PNG and file_format != Format.JPEG:
        raise InvalidFormat(f"invalid format: {file_format}")
    if img is None:
        raise FileLoadError(file_path, "failed to load image")
    print(f"Высота: {img.shape[0]}")
    print(f"Ширина: {img.shape[1]}")
    print(f"Каналы: {img.shape[2]}")
    print(f"Тип данных: {img.dtype}")
    return img

def convert_to_grayscale(img):
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayscaled.png', grayscaled)

def apply_median_filter(img, kernel_size=5):
    blured = cv2.medianBlur(img, kernel_size)
    cv2.imwrite('mediablured.png', blured)

def extract_roi(img: cv2.Mat, size=100):
    h, w = img.shape[:2]
    y_start, x_start = h//2 - size//2, w//2 - size//2
    roi = img[y_start:y_start+size, x_start:x_start+size]
    cv2.imwrite('roied.png', roi)

def invert_colors(img):
    inverted = cv2.bitwise_not(img)
    cv2.imwrite('inverted.png', inverted)