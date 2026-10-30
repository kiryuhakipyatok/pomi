import cv2
import numpy as np
import os

def create_test_image(filename='test_image.jpg'):
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (80, 80), (255, 255, 255), -1)
    cv2.circle(img, (140, 50), 30, (0, 0, 255), -1)
    cv2.line(img, (20, 120), (180, 180), (0, 255, 0), 1)
    cv2.putText(img, 'TEST', (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
    
    cv2.imwrite(filename, img)
    return filename

def resize_image(img, size=None, fx=None, fy=None, interpolation=cv2.INTER_LINEAR):
    if size is not None:
        if size[0] <= 0 or size[1] <= 0:
            raise ValueError("Размеры (ширина, высота) должны быть положительными числами.")
    elif fx is not None and fy is not None:
        if fx <= 0 or fy <= 0:
            raise ValueError("Коэффициенты масштабирования fx и fy должны быть > 0.")
    else:
        raise ValueError("Необходимо указать либо size, либо fx и fy.")

    return cv2.resize(img, dsize=size, fx=fx, fy=fy, interpolation=interpolation)

def compare_interpolation_methods(img, scale_factor=4.0):
    methods = {
        'NEAREST (Fast, Low Quality)': cv2.INTER_NEAREST,
        'LINEAR (Balanced)': cv2.INTER_LINEAR,
        'CUBIC (High Quality)': cv2.INTER_CUBIC,
        'LANCZOS4 (Best Quality)': cv2.INTER_LANCZOS4
    }
    
    results = {}
    for name, method in methods.items():
        resized = resize_image(img, fx=scale_factor, fy=scale_factor, interpolation=method)

        cv2.putText(resized, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.0, (255, 255, 255), 2, cv2.LINE_AA)
        results[name] = resized

    top_row = np.hstack((list(results.values())[0], list(results.values())[1]))
    bottom_row = np.hstack((list(results.values())[2], list(results.values())[3]))
    comparison_grid = np.vstack((top_row, bottom_row))
    
    return comparison_grid

if __name__ == '__main__':
    img_path = 'test_image.jpg'
    
    if not os.path.exists(img_path):
        create_test_image(img_path)
        
    img = cv2.imread(img_path)
    if img is None:
        print("Ошибка: файл не найден или не является изображением.")
        exit(1)
        
    print("[INFO] Сравнение методов интерполяции (увеличение x4)...")
    try:
        # Выполняем сравнение
        comparison_result = compare_interpolation_methods(img, scale_factor=4.0)
        
        # Сохраняем результат
        out_path = 'interpolation_comparison.jpg'
        cv2.imwrite(out_path, comparison_result)
        print(f"[SUCCESS] Сравнение успешно сохранено в файл: {out_path}")
        
    except ValueError as e:
        print(f"[ERROR] Ошибка значений: {e}")