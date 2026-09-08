from abc import ABC, abstractmethod
from enums import Format
from pathlib import Path
from exeptions import *
from image import Image


class MediaProcessor(ABC):
    @abstractmethod
    def process(self, file_path):
        pass
    
    @abstractmethod
    def validate(self, file_path):
        pass

class ImageProcessor(MediaProcessor):
    def process(self, image: Image, filters):
        try:
            for filter_obj in filters:
                filter_obj.apply(image)
        except FilterError as e:
            raise MediaError(str(e))
    
    def validate(self, file_path):
        file_format = Path(file_path).suffix
        if file_format != Format.PNG and file_format != Format.JPEG:
            raise InvalidFormat(f"invalid format: {file_format}")

        try:
            import cv2
            img = cv2.imread(file_path)
            if img is None:
                raise FileLoadError(file_path, "file is not image")
        except ImportError:
            raise MediaError("OpenCV is not installed", file_path)
        except Exception as e:
            raise FileLoadError(file_path, str(e))