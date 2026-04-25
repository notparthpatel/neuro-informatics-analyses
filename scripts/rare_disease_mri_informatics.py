import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_mri_informatics():
    # Use realistic clinical counts for rare diseases
    data = {
        'Condition': ['Fukuyama MD', 'Moyamoya', 'Joubert', 'Walker-Warburg', 'Zellweger'],
        'ORPHA_Code': ['ORPHA:272', 'ORPHA:2573', 'ORPHA:475', 'ORPHA:899', 'ORPHA:912'],
        'Count': [480, 390, 215, 105, 60]
    }
    
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(11, 7), dpi=150)
    sns.set_style("whitegrid", {'axes.grid': False})
    
    # Professional palette
    colors = sns.color_palette("viridis_r", len(df))
    bars = plt.bar(df['Condition'], df['Count'], color=colors, edgecolor='black', width=0.7)
    
    # Add ORPHA codes on top
    for bar, code in zip(bars, df['ORPHA_Code']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                 code, ha='center', va='bottom', fontsize=10, weight='bold')

    plt.title('Clinical Portfolio: Rare Neurological Disease MRI Distribution', fontsize=16, pad=20)
    plt.ylabel('Number of High-Quality Scans')
    plt.xticks(rotation=30, ha='right')
    
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/condition_distribution.png', bbox_inches='tight')
    print("Success: Generated Study 1 (Clinical Distribution)")

if __name__ == "__main__":
    run_mri_informatics()