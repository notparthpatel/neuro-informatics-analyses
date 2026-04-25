# Neuro Informatics Projects
**Developer:** Parth Patel
**Focus:** Clinical Informatics, Neurobehavioral Risk Modeling, and Imaging QA

This repository contains a multi-modal research pipeline designed to support clinical decision support systems. As an incoming BS/MD student at IU Indianapolis, I have developed these tools to demonstrate competency in handling both unstructured medical imaging data and structured clinical biomarkers using Python based informatics.

## Study 1: Rare Disease MRI Informatics
**Objective:** Validation of a curated MRI dataset for rare neurological conditions to ensure clinical utility in AI driven diagnostics.
* Standardized Mapping: Integrated Orphanet (ORPHA) clinical codes for conditions including Moyamoya and Walker Warburg Syndrome.
* Data Engineering: Automated metadata parser to verify class balance and stratified splitting across 2,000 high quality scans.
* Visual Evidence: ![MRI Distribution](results/condition_distribution.png)

## Study 2: MRI Image Quality Audit
**Objective:** Implementing automated image quality gatekeeping for neuroimaging pipelines.
* Automated QA: Developed an Image Quality Audit (IQA) script using Laplacian Variance to mathematically score scan sharpness.
* Technical Insight: This module ensures that only high fidelity scans enter the analytic pipeline, reducing noise in diagnostic models.
* Visual Evidence: ![Quality Audit](results/mri_quality_audit.png)

## Study 3: Neurobehavioral Risk Modeling
**Objective:** Analyzing the intersection of lifestyle stressors, systemic inflammation, and patient outcomes.
* Biomarker Correlation: Mapped interactions between Stress Levels, Sleep Duration, and C-Reactive Protein (CRP).
* Informatics Tool: Developed using Seaborn and Matplotlib for high fidelity statistical reporting.
* Visual Evidence: ![Correlation Heatmap](results/neuro_risk_heatmap.png)

## Study 4: Clinical Risk Stratification
**Objective:** Categorizing patients into actionable risk tiers based on composite biomarker scores.
* Clinical Stratification: Engineered a Neuro-Inflammatory Risk Index to categorize patients into Low, Moderate, and High Risk tiers.
* Implementation: This tool simulates a clinical decision support system used to identify high risk patients within an EMR framework.
* Visual Evidence: ![Risk Stratification](results/risk_stratification.png)

## Study 5: Machine Learning and Predictive Analytics
**Objective:** Quantifying the predictive weight of behavioral determinants on mental health risk.
* Predictive Modeling: Implemented a Random Forest pipeline using scikit-learn to identify specific risk drivers.
* Robust Logic: Built a column discovery loop to handle inconsistent clinical data headers and ensure model stability.
* Visual Evidence: ![Feature Importance](results/feature_importance.png)

## Technical Stack
* Languages: Python 3.12+
* Libraries: Pandas, NumPy, Scikit-learn, OpenCV (Headless), Seaborn, Matplotlib
* Informatics: Regenstrief style clinical data modeling and ORPHA code integration

## About Me
I am a BS/MD candidate and Bepko Scholar at IU Indianapolis with a long term interest in applying computational tools to improve diagnostic accuracy and patient centered brain health outcomes.

### Contact Information
- **LinkedIn:** linkedin/ln/notparthpatel
- **Email:** pvp4@iu.edu

