from image import Image
from mediaLibrary import MediaLibrary
import sys
import cv2
from matplotlib import pyplot as plt
from mediaProcessor import ImageProcessor
from mediaLoader import MediaLoader
from imageFilter import *

if __name__ == "__main__":
    filePath = "image.png"
    image1 = None
    try:
        image1 = Image(filePath)
    except Exception as e:
        print(f"error: {e}")
        sys.exit(0)
    
    res = image1.get_resolution()
    info = image1.get_info()
    colorSpace = image1.get_color_space()
    print(info)
    print(res)
    print(colorSpace)

    mediaLib = MediaLibrary()
    mediaLib.add(image1)
    mediaLib.add(image1)
    totalDur = mediaLib.get_total_duration()
    print(totalDur)
    filtered = mediaLib.filter_by_type(Image)
    print(filtered)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image1.mat, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')

    imageProcessor = ImageProcessor()
    mediaLoader = MediaLoader()
    try:
        brF = BrightnessFilter()
        cF = ContrastFilter()
        blF = BlurFilter()

        imageProcessor.validate(filePath)
        imageProcessor.process(image1, [brF, cF, blF])
        mediaLoader.load_image(filePath)
    except Exception as e:
        print(f"error: {e}")
        sys.exit(0)

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image1.mat, cv2.COLOR_BGR2RGB))
    plt.title('Lightened')
    plt.axis('off')

    plt.show()