import os
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

def run_analysis():
    # 1. Download/Fetch path
    path = kagglehub.dataset_download("ahsanneural/rare-neurological-diseases-mri-curated-edition")
    
    # 2. Point to the 'train' folder specifically to find the disease names
    # (The diseases are listed inside train, val, and test)
    data_dir = os.path.join(path, 'rare_neuro_mri_curated', 'train')
    
    stats = []
    if os.path.exists(data_dir):
        for condition in os.listdir(data_dir):
            condition_path = os.path.join(data_dir, condition)
            if os.path.isdir(condition_path):
                # Count how many MRI scans are in each disease folder
                file_count = len(os.listdir(condition_path))
                stats.append({"Condition": condition, "Scan_Count": file_count})
    
    if not stats:
        print(f"Still looking... searched in: {data_dir}")
        return

    # 3. Create a Professional Clinical Graph
    df = pd.DataFrame(stats)
    plt.figure(figsize=(12, 8))
    plt.bar(df['Condition'], df['Scan_Count'], color='#003366') # Deep Navy Clinical Blue
    
    plt.title('Clinical MRI Dataset: Scan Distribution by Neurological Condition', fontsize=14)
    plt.ylabel('Number of Scans (Training Set)', fontsize=12)
    plt.xlabel('Diagnosed Condition', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    # 4. Save
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/condition_distribution.png')
    print("Success! Disease-specific graph saved to results/condition_distribution.png")

if __name__ == "__main__":
    run_analysis()
