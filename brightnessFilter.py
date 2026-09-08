from imageFilter import ImageFilter
import cv2

class BrightnessFilter(ImageFilter):    
    def __init__(self, factor: float = 100):
        self.factor = factor
    
    def apply(self, image_data):
       cv2.convertScaleAbs(image_data.mat, image_data.mat, alpha=1.0, beta=self.factor)