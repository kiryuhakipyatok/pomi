from image import Image
from mediaLibrary import MediaLibrary
import sys
import cv2
from matplotlib import pyplot as plt
from mediaProcessor import ImageProcessor
from mediaLoader import MediaLoader
from imageFilter import *
from mediaCollection import *
from imageProcessor import *

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
    print(f"Info: {info}")
    print(f"Resolution: {res}")
    print(f"Color Space: {colorSpace}")

    mediaLib = MediaLibrary()
    mediaLib.add(image1)
    mediaLib.add(image1)
    totalDur = mediaLib.get_total_duration()
    print(f"Total duration: {totalDur}")
    filtered = mediaLib.filter_by_type(Image)
    print(f"MediaLibrary filtered: {filtered}")

    collection = MediaCollection[Image]()
    collection.add(image1)
    collection.add("not_an_image")

    print(f"Отфильтровано по Image: {collection.filter_by_type(Image)}")

    meta = MediaMetadata(filePath)
    meta.set_metadata('width', res[0] if isinstance(res, (tuple, list)) else 1920)
    meta.set_metadata('height', res[1] if isinstance(res, (tuple, list)) else 1080)
    meta.set_metadata('color_space', colorSpace)
    print(f"Ключ 'width' существует: {meta.get_metadata('width')}")
    print(f"Ключ 'author' существует: {meta.get_metadata('author')}")
    print(f"Словарь метаданных: {meta.metadata}")

    analyzer = MetadataAnalyzer()
    analyzer.analyze_file(filePath, meta.metadata)
    summary = analyzer.get_summary()
    print(f"Сводка анализатора (summary): {summary}")

    sample_media_items = [
        {'id': 1, 'width': 1920, 'height': 1080, 'color_space': 'RGB', 'created_date': 1700000000},
        {'id': 2, 'width': 800,  'height': 600,  'color_space': 'GRAY', 'created_date': 1710000000},
        {'id': 3, 'width': 3840, 'height': 2160, 'color_space': 'RGB', 'created_date': 1690000000},
        {'id': 4, 'width': 1280, 'height': 720,  'color_space': 'RGBA', 'created_date': 1705000000},
    ]
    media_filter = MediaFilter(sample_media_items)

    res_filtered = media_filter.filter_by_resolution(1920, 1080)
    print(f"Фильтр по разрешению (<= 1920x1080): {[item['id'] for item in res_filtered]}")

    date_sorted = media_filter.sort_by_date(reverse=True)
    print(f"Сортировка по дате (desc): {[item['id'] for item in date_sorted]}")

    grouped = media_filter.group_by_color_space()
    print(f"Группировка по color_space: { {k: len(v) for k, v in grouped.items()} }")

    try:
        loadedImg = load_image("chad.png")
        convert_to_grayscale(loadedImg)
        apply_median_filter(loadedImg)
        extract_roi(loadedImg,100)
        invert_colors(loadedImg)
    except Exception as e:
        print(f"error: {e}")
    

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
    plt.title('Filtered')
    plt.axis('off')

    plt.show()