from exeptions import *

class MediaLoader:
    def load_image(self, file_path):
        try:
            import cv2
            img = cv2.imread(file_path)
            if img is None:
                raise FileLoadError(file_path, "file is not image")
            return img
        except ImportError:
            raise MediaError("OpenCV is not installed", file_path)
        except Exception as e:
            raise FileLoadError(file_path, str(e))