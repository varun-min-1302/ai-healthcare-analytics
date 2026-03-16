# Phase 3 - ML Model Training Guide

## Overview
Train, tune, and save classification models for all three diseases using PyCaret AutoML.

## Training Notebooks Created

### 1. Diabetes Model (`notebooks/04_diabetes_training.ipynb`)
- Dataset: PIMA Indians Diabetes (768 rows, 8 features)
- Target: Outcome (0/1)
- Strategy: AutoML with `fix_imbalance=True` for class imbalance
- Expected AUC: ≥ 0.85

### 2. Heart Disease Model (`notebooks/05_heart_training.ipynb`)
- Dataset: Cleveland Heart Disease (303 rows, 13 features)
- Target: target (0/1)
- Categorical features: sex, cp, fbs, restecg, exang, slope, ca, thal
- Expected AUC: ≥ 0.85

### 3. CKD Model (`notebooks/06_ckd_training.ipynb`)
- Dataset: Chronic Kidney Disease (400 rows, 24 features)
- Target: classification (ckd/notckd)
- Categorical features: rbc, pc, pcc, ba, htn, dm, cad, appet, pe, ane
- Expected AUC: ≥ 0.85

## PyCaret 5-Step Pipeline

Each notebook follows this workflow:

```python
# 1. Setup experiment
exp = setup(data, target='...', session_id=42, normalize=True)

# 2. Compare models (AutoML)
best = compare_models(sort='AUC', n_select=1)

# 3. Tune hyperparameters
tuned = tune_model(best, optimize='AUC', n_iter=50, search_library='optuna')

# 4. Evaluate performance
evaluate_model(tuned)

# 5. Finalize and save
final = finalize_model(tuned)
save_model(final, 'models/disease_model')
```

## Modules Created

### `src/predictor.py`
- `DiseasePredictor` class for loading models and generating predictions
- `load_model()` - Load individual disease model
- `load_all_models()` - Load all available models
- `predict()` - Generate prediction for single disease
- `predict_all()` - Generate predictions for all diseases

### `src/explainer.py`
- `ModelExplainer` class for SHAP-based explanations
- `load_explainer()` - Cached function to load model and create SHAP explainer
- `explain_prediction()` - Generate SHAP values and waterfall plot
- `get_top_features()` - Extract top contributing features
- `generate_explanation_text()` - Plain-language explanation

### `src/risk_engine.py`
- `RiskResult` dataclass for structured risk assessment
- `classify_risk()` - Convert probability to Low/Medium/High tier
- `get_recommendation()` - Clinical recommendations per disease/tier
- `format_alert_message()` - Alert message formatting

## Risk Stratification Thresholds

```python
THRESHOLDS = {
    'low_max': 0.35,    # < 0.35 = Low Risk
    'high_min': 0.65    # ≥ 0.65 = High Risk
}
# 0.35 - 0.65 = Medium Risk
```

## Training Workflow

### Step 1: Download Datasets
1. PIMA Diabetes: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
2. Heart Disease: https://archive.ics.uci.edu/ml/datasets/heart+disease
3. CKD: https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease

### Step 2: Run EDA Notebooks (Phase 2)
- `01_diabetes_eda.ipynb`
- `02_heart_eda.ipynb`
- `03_ckd_eda.ipynb`

### Step 3: Train Models in Google Colab
1. Open `04_diabetes_training.ipynb` in Colab
2. Mount Google Drive
3. Upload diabetes.csv
4. Run all cells
5. Download `diabetes_model.pkl` to local `models/` folder
6. Repeat for heart and CKD

### Step 4: Verify Models Locally
```bash
python tests/test_predictor.py
```

## SHAP Integration

After training, each model includes SHAP explainability:

```python
# Extract base estimator
base_model = pipeline.steps[-1][1]

# Create explainer
explainer = shap.TreeExplainer(base_model)

# Generate SHAP values
shap_values = explainer(X_test)

# Waterfall plot
shap.plots.waterfall(shap_values[0])
```

## Success Criteria

- [ ] All 3 models trained with AUC ≥ 0.85
- [ ] Models saved as .pkl files in `models/` directory
- [ ] SHAP explainers verified for each model
- [ ] Risk engine tested with sample data
- [ ] Predictor module loads all models successfully

## Next Steps (Phase 4)

Once models are trained:
1. Build Streamlit dashboard UI
2. Integrate predictor and explainer modules
3. Add risk visualization components
4. Implement alert system for high-risk cases
