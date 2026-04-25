import os
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def run_ml_model():
    # 1. Load Data
    path = kagglehub.dataset_download("mdmahfuzsumon/neurobehavior-clinical-health-risk-sample-dataset")
    
    # Get the main CSV
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    # Avoid tiny files, pick the one with actual data
    main_file = max([os.path.join(path, f) for f in files], key=os.path.getsize)
    df = pd.read_csv(main_file)

    # 2. Clean headers
    df.columns = df.columns.str.strip()

    # 3. SELECT THE BEST TARGET
    # We look for 'Mental_Health_Risk' first, then fall back to 'Stress_Level'
    potential_targets = ['Mental_Health_Risk', 'Stress_Level', 'Cortisol_Risk', 'Mood_Score']
    target = next((col for col in potential_targets if col in df.columns), None)

    if not target:
        print(f"Error: Could not find a target. Available columns: {df.columns.tolist()}")
        return

    # 4. SELECT FEATURES
    features = ['Age', 'Sleep_Hours', 'Screen_Time_Hours', 'Physical_Activity', 
                'Meditation_Minutes', 'Social_Interaction', 'Rumination_Score']
    
    # Only use what exists
    existing_features = [f for f in features if f in df.columns]
    
    X = df[existing_features]
    y = df[target]

    # 5. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 6. Build the Model (Using Regressor for more granular importance)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 7. Extract Feature Importance
    importances = model.feature_importances_
    feat_df = pd.DataFrame({'Feature': existing_features, 'Importance': importances})
    feat_df = feat_df.sort_values(by='Importance', ascending=True)

    # 8. Visualization
    plt.figure(figsize=(10, 6))
    plt.barh(feat_df['Feature'], feat_df['Importance'], color='#3498db', edgecolor='black')
    plt.title(f'Predictive Weight of Lifestyle Factors on {target.replace("_", " ")}', fontsize=14)
    plt.xlabel('Importance Score (Random Forest)')
    plt.tight_layout()

    # 9. Save
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/feature_importance.png')
    print(f"Success! Model trained using '{target}' as the clinical outcome.")
    print(f"Features analyzed: {len(existing_features)}")

if __name__ == "__main__":
    run_ml_model()