from imageFilter import ImageFilter
import cv2

class BrightnessFilter(ImageFilter):    
    def __init__(self, factor: float = 1.5):
        self.factor = factor
    
    def apply(self, image_data):
        image = cv2.imread(image_data.filename)
        brighted = cv2.convertScaleAbs(image, alpha=1.0, beta=self.factor)
        return brighted