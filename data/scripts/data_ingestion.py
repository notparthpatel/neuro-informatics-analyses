import kagglehub
import os
import shutil

def fetch_dataset():
    print("Fetching Neurological MRI Dataset from Kaggle...")
    # Downloads to a temporary cache
    cache_path = kagglehub.dataset_download("ahsanneural/rare-neurological-diseases-mri-curated-edition")
    
    print(f"Dataset downloaded to: {cache_path}")
    return cache_path

if __name__ == "__main__":
    fetch_dataset()
