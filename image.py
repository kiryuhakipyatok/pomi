from mediaObject import MediaObject
from enum import StrEnum
from pathlib import Path
import cv2

class Format(StrEnum):
    PNG = ".png"
    JPEG = ".jpeg"

class InvalidFormat(Exception):
    pass

class Image(MediaObject):
    def __init__(self, filename):
        super().__init__(filename, duration=0)
        file_format = Path(filename).suffix
        if file_format != Format.PNG and file_format != Format.JPEG:
            raise InvalidFormat(f"invalid format: {file_format}")

        mat = cv2.imread(filename)
        self.height, self.width, self.channels = mat.shape
        self.mat = mat
    
    def get_resolution(self):
        return f"{self.width}x{self.height}"

    def get_color_space(self):
        return f"BRG: {self.channels} channels"
    
    def get_info(self):
        info = super().get_info()
        return f"{info}, {self.get_resolution()}"