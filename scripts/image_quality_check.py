import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt

def calculate_sharpness(image_path):
    # Uses the Laplacian Variance method to detect blur
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None: return None
    return cv2.Laplacian(img, cv2.CV_64F).var()

def run_quality_check():
    # Path to your MRI data folder
    mri_path = 'data/mri_images/' # Update this to where your .png files are
    
    if not os.path.exists(mri_path):
        print("Point the mri_path to your actual images folder.")
        return

    scores = []
    for img_name in os.listdir(mri_path)[:100]: # Check first 100 images
        val = calculate_sharpness(os.path.join(mri_path, img_name))
        if val: scores.append(val)

    # Plot Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(scores, bins=20, color='skyblue', edgecolor='black')
    plt.title('Informatics Pipeline: MRI Image Sharpness Distribution (Laplacian Variance)')
    plt.xlabel('Sharpness Score')
    plt.ylabel('Scan Count')

    os.makedirs('results', exist_ok=True)
    plt.savefig('results/mri_quality_audit.png')
    print("Success: MRI Quality Audit complete.")

if __name__ == "__main__":
    run_quality_check()