import os
import pandas as pd
import matplotlib.pyplot as plt
from data_ingestion import fetch_dataset

def run_analysis():
    path = fetch_dataset()
    stats = []

    # Iterate through folders (Conditions)
    for condition in os.listdir(path):
        condition_path = os.path.join(path, condition)
        if os.path.isdir(condition_path):
            file_count = len(os.listdir(condition_path))
            stats.append({"Condition": condition, "Scan_Count": file_count})

    # Convert to Dataframe
    df = pd.DataFrame(stats)
    
    # Create Visualization
    plt.figure(figsize=(10, 6))
    plt.bar(df['Condition'], df['Scan_Count'], color='#2c3e50')
    plt.title('Clinical Dataset Composition: Rare Neurological Conditions', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Number of Available Scans')
    
    # Save the result to our results folder
    plt.tight_layout()
    plt.savefig('results/condition_distribution.png')
    print("Analysis complete. Graph saved to results/folder.")

if __name__ == "__main__":
    run_analysis()
