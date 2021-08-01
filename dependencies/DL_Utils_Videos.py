import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

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

    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
    ttime = cap.get(cv2.CAP_PROP_POS_MSEC)*seq.shape[0]/1000

    print(f"El tiempo total del video es {ttime}")
    print(f"El número de frames por segundos es {seq.shape[0]/ttime}")

    return None

def plot_frames(seq, m=3, n=3, figsize = (15,15)):
    total = m*n  
    frames_idx = list(np.arange(0,75,1))
    sub_frames_idx = random.sample(frames_idx, total)
    sub_frames_idx.sort()
    fig, ax = plt.subplots(m, n, figsize = figsize)
    
    for i, ax in enumerate(ax.flat):
        if i <= len(sub_frames_idx):
            ax.imshow(seq[sub_frames_idx[i]])
            ax.set_title(f"Frame Number {sub_frames_idx[i]}")
        else:
            continue
        
    return None   
