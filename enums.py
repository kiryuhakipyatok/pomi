from enum import StrEnum

class Format(StrEnum):
    PNG = ".png"
    JPEG = ".jpeg"

class Filter(StrEnum):
    BRIGHTNESS_FILTER = "brightness filter"
    CONTRAST_FILTER = "contrast filter"
    BLUR_FILTER = "blur_filter"