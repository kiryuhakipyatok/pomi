import cv2
import numpy as np

def create_synthetic_frames():

    frame1 = np.zeros((240, 320), dtype=np.uint8)
    frame2 = np.zeros((240, 320), dtype=np.uint8)

    cv2.rectangle(frame1, (100, 100), (140, 140), 255, -1)
    cv2.rectangle(frame2, (110, 105), (150, 145), 255, -1)
    
    return frame1, frame2

def compute_sad(block1, block2):
    return np.sum(np.abs(block1.astype(np.int32) - block2.astype(np.int32)))

def find_best_block(prev_frame, block, start_x, start_y, search_range=16):
    h, w = prev_frame.shape
    bh, bw = block.shape
    
    min_sad = float('inf')
    best_dx, best_dy = 0, 0

    min_x = max(0, start_x - search_range)
    max_x = min(w - bw, start_x + search_range)
    min_y = max(0, start_y - search_range)
    max_y = min(h - bh, start_y + search_range)
    
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            ref_block = prev_frame[y:y+bh, x:x+bw]
            sad = compute_sad(block, ref_block)
            
            if sad < min_sad:
                min_sad = sad
                best_dx = x - start_x
                best_dy = y - start_y
                
    return best_dx, best_dy

def estimate_block_motion(prev_frame, curr_frame, block_size=16, search_range=16):
    h, w = curr_frame.shape
    motion_vectors = []

    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            block = curr_frame[y:y+block_size, x:x+block_size]

            if np.std(block) < 5.0:
                continue
                
            dx, dy = find_best_block(prev_frame, block, x, y, search_range)

            if dx != 0 or dy != 0:
                motion_vectors.append((x, y, dx, dy))
                
    return motion_vectors

def visualize_motion_vectors(img, vectors, block_size):
    result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img.copy()
    
    for (x, y, dx, dy) in vectors:
        start_pt = (x + block_size // 2, y + block_size // 2)
        end_pt = (start_pt[0] + dx, start_pt[1] + dy)
        
        cv2.arrowedLine(result, start_pt, end_pt, (0, 255, 0), 1, tipLength=0.3)
        cv2.rectangle(result, (x, y), (x + block_size, y + block_size), (255, 0, 0), 1)
        
    return result

def test_different_block_sizes(prev_frame, curr_frame):
    """Сравнивает результаты оценки движения для блоков 8x8, 16x16 и 32x32."""
    block_sizes = [8, 16, 32]
    
    for size in block_sizes:
        print(f"[INFO] Выполняется поиск для блоков {size}x{size}... (это может занять несколько секунд)")
        vectors = estimate_block_motion(prev_frame, curr_frame, block_size=size, search_range=16)
        print(f"       Найдено векторов движения: {len(vectors)}")
        
        result_img = visualize_motion_vectors(curr_frame, vectors, size)
        
        cv2.putText(result_img, f'Block size: {size}x{size}', (10, 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                    
        out_filename = f'block_matching_{size}x{size}.jpg'
        cv2.imwrite(out_filename, result_img)
        print(f"[SUCCESS] Сохранено в {out_filename}")

if __name__ == '__main__':
    prev_frame, curr_frame = create_synthetic_frames()
    
    print("--- Запуск оценки движения по блокам (Block Matching) ---")
    test_different_block_sizes(prev_frame, curr_frame)
    print("--- Анализ завершен ---")