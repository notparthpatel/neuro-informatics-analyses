import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

def run_health_analysis():
    # 1. Download the new dataset
    path = kagglehub.dataset_download("mdmahfuzsumon/neurobehavior-clinical-health-risk-sample-dataset")
    
    # 2. Find the CSV (it might be in a subfolder or named slightly differently)
    csv_file = "NeuroBehavior-Clinical Health Risk Sample Dataset.csv"
    full_path = os.path.join(path, csv_file)
    
    if not os.path.exists(full_path):
        # Fallback if the filename varies
        files = [f for f in os.listdir(path) if f.endswith('.csv')]
        full_path = os.path.join(path, files[0])

    df = pd.read_csv(full_path)

    # 3. Create a Correlation Heatmap of Neuro-Behavioral Markers
    # This shows if high stress actually links to higher CRP (inflammation)
    plt.figure(figsize=(12, 8))
    cols_to_analyze = ['Stress_Level', 'Sleep_Hours', 'Rumination_Score', 
                       'Focus_Level', 'Mood_Score', 'CRP', 'Fasting_Glucose']
    
    correlation_matrix = df[cols_to_analyze].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    
    plt.title('Neuro-Behavioral Correlation Matrix: Stress vs. Clinical Markers')
    
    # 4. Save the result
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/neuro_risk_heatmap.png')
    
    # 5. Print a quick insight for your README
    print("\n--- Clinical Insights ---")
    avg_stress = df['Stress_Level'].mean()
    print(f"Average Cohort Stress Level: {avg_stress:.2f}/10")
    print("Heatmap saved to results/neuro_risk_heatmap.png")

if __name__ == "__main__":
    run_health_analysis()