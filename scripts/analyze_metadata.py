import os
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

def run_professional_analysis():
    # 1. Download/Fetch path
    path = kagglehub.dataset_download("ahsanneural/rare-neurological-diseases-mri-curated-edition")
    
    # 2. Point to the specific subfolder where the CSVs live
    # This was the missing piece!
    base_data_path = os.path.join(path, 'rare_neuro_mri_curated')
    metadata_path = os.path.join(base_data_path, 'metadata.csv')
    
    # Check if the file exists before reading to prevent the error
    if not os.path.exists(metadata_path):
        print(f"Error: Could not find metadata.csv at {metadata_path}")
        return

    # 3. Load the official clinical metadata
    df_meta = pd.read_csv(metadata_path)
    
    # 4. Create the summary
    summary = df_meta.groupby(['full_name', 'orphacode']).size().reset_index(name='scan_count')
    
    # 5. Create the Research-Grade Visualization
    plt.figure(figsize=(14, 8))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    bars = plt.bar(summary['full_name'], summary['scan_count'], color=colors, edgecolor='black', alpha=0.8)
    
    for i, bar in enumerate(bars):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, 
                 f"{summary['orphacode'][i]}", 
                 ha='center', va='bottom', fontweight='bold')

    plt.title('Clinical Portfolio: Rare Neurological Disease MRI Distribution', fontsize=16, pad=20)
    plt.ylabel('Number of High-Quality Scans', fontsize=12)
    plt.xticks(rotation=30, ha='right')
    plt.ylim(0, 450)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    plt.figtext(0.15, 0.8, "Dataset Features:\n• Balanced Classes (400/ea)\n• Quality-Curated\n• ORPHA Code Indexed", 
                bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})

    plt.tight_layout()
    
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/condition_distribution.png', dpi=300)
    print("Success! Research-grade graph saved with clinical ORPHA codes.")

if __name__ == "__main__":
    run_professional_analysis()