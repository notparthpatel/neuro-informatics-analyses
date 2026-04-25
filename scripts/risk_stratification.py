import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

def run_stratification():
    # 1. Load Data
    path = kagglehub.dataset_download("mdmahfuzsumon/neurobehavior-clinical-health-risk-sample-dataset")
    
    # Ensure we get the actual data file, not the tiny metadata/submission files
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    main_file = max([os.path.join(path, f) for f in files], key=os.path.getsize)
    df = pd.read_csv(main_file)
    
    # 2. Clean headers
    df.columns = df.columns.str.strip()

    # 3. Safe Column Mapping
    # Fallback logic: if 'Stress_Level' is missing, it uses 'Cortisol_Risk' or similar
    s_col = next((c for c in ['Stress_Level', 'Cortisol_Risk'] if c in df.columns), None)
    c_col = next((c for c in ['CRP', 'Inflammation'] if c in df.columns), None)
    sl_col = next((c for c in ['Sleep_Hours', 'Sleep'] if c in df.columns), None)
    m_col = next((c for c in ['Mood_Score', 'Mental_Health_Risk'] if c in df.columns), None)

    if not all([s_col, c_col, sl_col]):
        print(f"Missing necessary columns for index. Available: {df.columns.tolist()}")
        return

    # 4. Create the Neuro-Inflammatory Risk Index
    # Normalized weights for clinical stratification
    df['Risk_Score'] = (df[s_col] * 0.4) + (df[c_col] * 0.4) - (df[sl_col] * 0.2)
    
    # 5. Define Tiers (High, Medium, Low)
    df['Risk_Tier'] = pd.qcut(df['Risk_Score'], q=3, labels=['Low Risk', 'Moderate Risk', 'High Risk'])

    # 6. Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Risk_Tier', y=m_col if m_col else 'Risk_Score', data=df, palette='coolwarm')
    plt.title('Clinical Stratification: Risk Tier Analysis', fontsize=14)
    plt.xlabel('Patient Risk Category')
    plt.ylabel('Outcome Measure' if m_col else 'Composite Risk Score')

    # 7. Save
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/risk_stratification.png')
    print(f"Success! Stratified {len(df)} patients into Risk Tiers.")

if __name__ == "__main__":
    run_stratification()