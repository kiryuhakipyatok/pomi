from abc import ABC, abstractmethod


class ImageFilter(ABC):
    @abstractmethod
    def apply(self, image_data):
        pass