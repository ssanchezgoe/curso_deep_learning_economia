import cv2
import numpy as np

def load_video(path, max_frames=0, resize=(224, 224)):
    cap = cv2.VideoCapture(path)
    frames = []
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = frame[:, :, [2, 1, 0]]
            frames.append(frame)

            if len(frames) == max_frames:
                break
    finally:
        cap.release()
    return np.array(frames)

def video_info(path):
    seq = load_video(path)
    print(f"Profundidad de pixel {seq.dtype}")
    print(f"Valores (min, max): ({np.min(seq)},{np.max(seq)})")
    print(f"Dimensiones del video: {seq.shape}")
    print(f"Total Pixeles: {seq.ravel().shape}")
    return None
