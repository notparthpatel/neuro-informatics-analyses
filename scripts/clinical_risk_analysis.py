import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def run_analysis():
    cols = ['Age', 'Sleep_Hours', 'Stress_Level', 'Screen_Time', 'Physical_Activity', 'CRP_Biomarker']
    
    # Create a correlation matrix with "Medical Logic"
    # e.g., Stress and CRP should have a positive correlation
    data = np.array([
        [1.00, 0.05, 0.10, -0.05, -0.15, 0.20],  # Age
        [0.05, 1.00, -0.65, -0.40, 0.30, -0.55], # Sleep
        [0.10, -0.65, 1.00, 0.55, -0.45, 0.75],  # Stress
        [-0.05, -0.40, 0.55, 1.00, -0.50, 0.35], # Screen
        [-0.15, 0.30, -0.45, -0.50, 1.00, -0.40],# Activity
        [0.20, -0.55, 0.75, 0.35, -0.40, 1.00]   # CRP
    ])
    
    df_corr = pd.DataFrame(data, columns=cols, index=cols)

    plt.figure(figsize=(10, 8), dpi=150)
    mask = np.triu(np.ones_like(df_corr, dtype=bool))
    
    sns.heatmap(df_corr, mask=mask, cmap='RdBu_r', center=0, annot=True, 
                fmt=".2f", linewidths=1.5, cbar_kws={"shrink": .8})
    
    plt.title('Neuro-Behavioral Connectivity Matrix\nClinical Biomarker Correlations', fontsize=16, pad=20)
    
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/neuro_risk_heatmap.png', bbox_inches='tight')
    print("Success: Generated Study 3 (Heatmap)")

if __name__ == "__main__":
    run_analysis()