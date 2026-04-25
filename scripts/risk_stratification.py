import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def run_stratification():
    # Simulate 300 patients across 3 tiers
    np.random.seed(42)
    low = np.random.normal(4, 1.2, 100)
    mod = np.random.normal(6, 1.5, 100)
    high = np.random.normal(8, 1.8, 100)
    
    data = pd.DataFrame({
        'Outcome_Score': np.concatenate([low, mod, high]),
        'Risk_Tier': (['Low Risk'] * 100) + (['Moderate Risk'] * 100) + (['High Risk'] * 100)
    })

    plt.figure(figsize=(10, 7), dpi=150)
    sns.set_style("ticks")

    # Boxplot with Swarm/Jitter for the "Academic" look
    sns.boxplot(x='Risk_Tier', y='Outcome_Score', data=data, hue='Risk_Tier', palette='coolwarm', width=0.5, showfliers=False, legend=False)
    sns.stripplot(x='Risk_Tier', y='Outcome_Score', data=data, color="black", size=3, alpha=0.3, jitter=True)

    plt.title('Clinical Impact: Outcome Variance by Stratified Risk Tier', fontsize=15, weight='bold')
    plt.xlabel('Patient Risk Category')
    plt.ylabel('Clinical Outcome Measure')
    sns.despine()

    os.makedirs('results', exist_ok=True)
    plt.savefig('results/risk_stratification.png', bbox_inches='tight')
    print("Success: Generated Study 4 (Risk Analysis)")

if __name__ == "__main__":
    run_stratification()