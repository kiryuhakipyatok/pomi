from abc import ABC, abstractmethod
from exeptions import *
from enums import Filter
from image import Image

class ImageFilter(ABC):
    @abstractmethod
    def apply(self, image_data):
        pass

class BrightnessFilter(ImageFilter):
    def __init__(self, factor: float =100):
        self.factor = factor
    
    def apply(self, image_data: Image):
        try:
            import cv2
            cv2.convertScaleAbs(image_data.mat, image_data.mat, alpha=1.0, beta=self.factor)
        except Exception as e:
            raise FilterError(image_data.filename, Filter.BRIGHTNESS_FILTER)

class ContrastFilter(ImageFilter):
    def __init__(self, factor: float = 1.5):
        self.factor = factor
    
    def apply(self, image_data: Image):
        try:
            import cv2
            cv2.convertScaleAbs(image_data.mat, image_data.mat, alpha=self.factor, beta=1.0)
        except Exception as e:
            raise FilterError(image_data.filename, Filter.CONTRAST_FILTER)


class BlurFilter(ImageFilter):
    def __init__(self, kernel_size: int = 33):
        if kernel_size % 2==0:
            raise CreateFilterError(None, Filter.BLUR_FILTER)
        self.kernel_size = kernel_size
    
    def apply(self, image_data: Image):
        try:
            import cv2
            cv2.GaussianBlur(image_data.mat, (self.kernel_size, self.kernel_size), 0, image_data.mat)
        except Exception as e:
            raise FilterError(image_data.filename, Filter.BLUR_FILTER)