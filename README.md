# 🏥 AI-Driven Healthcare Analytics Platform

Explainable Multi-Disease Risk Prediction using Machine Learning and SHAP

## Overview

This platform leverages AutoML (PyCaret) and Explainable AI (SHAP) to predict disease risk across multiple conditions:
- Type 2 Diabetes
- Heart Disease  
- Chronic Kidney Disease

## Features

- 📊 Interactive web dashboard (Streamlit)
- 🤖 Automated model training with PyCaret
- 🔍 SHAP-powered prediction explanations
- ⚠️ Real-time risk alerts for high-risk patients
- 📈 Model performance metrics and visualizations
- 📁 CSV batch processing support

## Project Structure

```
healthai-platform/
├── app.py                  # Streamlit application entry point
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml        # UI theme configuration
├── src/
│   ├── data_processor.py  # Data preprocessing pipeline
│   ├── predictor.py       # Model loading and prediction
│   ├── explainer.py       # SHAP explanation generation
│   └── risk_engine.py     # Risk stratification logic
├── models/                 # Trained model files (.pkl)
├── notebooks/              # Google Colab training notebooks
└── data/sample/           # Sample CSV files for testing
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/healthai-platform.git
cd healthai-platform
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Models (Google Colab)

1. Open `notebooks/training_template.ipynb` in Google Colab
2. Duplicate for each disease module (diabetes, heart, ckd)
3. Follow the PyCaret training workflow
4. Download trained `.pkl` files to `models/` directory

### 4. Run Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

## Technology Stack

- **AutoML**: PyCaret 3.3.2
- **Explainability**: SHAP 0.45.1
- **Web Framework**: Streamlit 1.32.0
- **Data Processing**: Pandas 2.2.1
- **Visualization**: Matplotlib, Plotly

## Datasets

All training data sourced from UCI Machine Learning Repository:
- PIMA Indians Diabetes Dataset
- Cleveland Heart Disease Dataset
- Chronic Kidney Disease Dataset

## Disclaimer

⚠️ **This tool is for informational purposes only.**  
Consult a licensed physician for medical diagnosis and treatment.

## License

MIT License

## Author

Developed as part of the AI-Driven Healthcare Analytics MVP project.

---

**Status**: Phase 1 Complete ✓  
**Next Steps**: Model training (Weeks 1-5)
