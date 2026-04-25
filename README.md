# Neuro Informatics Project Showcase

**Developer:** Parth Patel

This repository contains a multi-modal research pipeline designed to support clinical decision support systems. As an incoming BS/MD student at IU Indianapolis, I have developed these tools to demonstrate competency in handling both unstructured medical imaging data and structured clinical biomarkers using Python based informatics.

## Study 1: Rare Disease MRI Informatics
**Objective:** Validation of a curated MRI dataset for rare neurological conditions to ensure clinical utility in AI driven diagnostics.
* Standardized Mapping: Integrated Orphanet (ORPHA) clinical codes for conditions including Moyamoya, Walker Warburg, and Fukuyama Muscular Dystrophy.
* Clinical Realism: The distribution reflects varied clinical prevalence rates observed in rare disease cohorts, providing a realistic baseline for informatics training.
* Visual Evidence: ![MRI Distribution](results/condition_distribution.png)

## Study 2: MRI Image Quality Audit
**Objective:** Implementing automated image quality gatekeeping using Laplacian Variance edge detection.
* Automated QA: Developed a Kernel Density Estimate (KDE) distribution model to mathematically score and visualize scan sharpness.
* Technical Insight: This module ensures that only high fidelity scans enter the analytic pipeline, simulating the data cleaning requirements of a professional radiology lab.
* Visual Evidence: ![Quality Audit](results/mri_quality_audit.png)

## Study 3: Neurobehavioral Risk Modeling
**Objective:** Analyzing the interaction between lifestyle stressors, systemic inflammation, and patient outcomes.
* Connectivity Map: Generated a high contrast correlation matrix mapping Stress Levels, Sleep Duration, and C-Reactive Protein (CRP).
* Informatics Tool: Built using a professional Spectral color palette to identify multi-variate interactions within behavioral health datasets.
* Visual Evidence: ![Correlation Heatmap](results/neuro_risk_heatmap.png)

## Study 4: Clinical Risk Stratification
**Objective:** Categorizing patients into actionable risk tiers using population density modeling.
* Swarm Plot Integration: Implemented a boxplot with a stripplot overlay to visualize individual patient variance across stratified risk categories.
* Clinical Application: This tool identifies high risk patients within a population health framework, allowing for targeted implementation of brain health interventions.
* Visual Evidence: ![Risk Stratification](results/risk_stratification.png)

## Study 5: Machine Learning and Predictive Analytics
**Objective:** Quantifying the predictive weight of behavioral determinants on mental health risk.
* Predictive Modeling: Implemented a Random Forest pipeline to identify specific risk drivers within neurobehavioral cohorts.
* Robust Logic: Built a column discovery loop to handle inconsistent clinical data headers and ensure model stability across different dataset versions.
* Visual Evidence: ![Feature Importance](results/feature_importance.png)

## Technical Stack
* Languages: Python 3.12+
* Libraries: Pandas, NumPy, Scikit-learn, OpenCV (Headless), Seaborn, Matplotlib
* Informatics: Regenstrief style clinical data modeling and ORPHA code integration

## About Me
I am a BS/MD candidate and Bepko Scholar at IU Indianapolis with an aim to apply computational tools to improve diagnostic accuracy and patient centered brain health outcomes.

### Contact Information
- **LinkedIn:** linkedin/ln/notparthpatel
- **Email:** pvp4@iu.edu