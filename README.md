# 🏥 AI-Driven Healthcare Analytics Platform

Explainable Multi-Disease Risk Prediction using Machine Learning and SHAP

![Status](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red)
![PyCaret](https://img.shields.io/badge/PyCaret-3.3.2-orange)
![SHAP](https://img.shields.io/badge/SHAP-0.45.1-purple)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)

## 🔗 Live Demo

> **Coming Soon**: Deploy to Streamlit Cloud and add your URL here  
> `https://your-app.streamlit.app`

## 🎯 Overview

This platform leverages AutoML (PyCaret) and Explainable AI (SHAP) to predict disease risk across multiple conditions with interpretable, clinician-friendly explanations.

### Supported Disease Modules
- 🩺 **Type 2 Diabetes** - PIMA Indians Dataset
- ❤️ **Heart Disease** - Cleveland Heart Disease Dataset  
- 🫘 **Chronic Kidney Disease** - CKD Dataset

## ✨ Features

- 📊 **Interactive Web Dashboard** - Modern Streamlit interface
- 🤖 **Automated ML Training** - PyCaret AutoML pipeline
- 🔍 **SHAP Explanations** - Understand what drives each prediction
- ⚠️ **Real-time Risk Alerts** - Automatic high-risk patient flagging
- 📈 **Model Performance Metrics** - AUC, accuracy, F1 scores
- 📁 **Batch CSV Processing** - Analyze multiple patients at once
- ✏️ **Manual Data Entry** - Interactive forms for single patients
- 🎨 **Modern Dark Theme** - Healthcare-branded UI

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.10+
pip or conda
```

### Installation

1. **Clone Repository**
```bash
git clone https://github.com/<your-username>/healthai-platform.git
cd healthai-platform
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run Application**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
healthai-platform/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .streamlit/
│   └── config.toml            # UI theme configuration
├── pages/                      # Dashboard pages
│   ├── input_page.py          # Patient data input
│   ├── dashboard.py           # Risk assessment results
│   ├── explainer.py           # SHAP visualizations
│   ├── performance.py         # Model metrics
│   └── about.py               # Project information
├── src/                        # Core modules
│   ├── data_processor.py      # Data preprocessing
│   ├── predictor.py           # Model loading & prediction
│   ├── explainer.py           # SHAP integration
│   └── risk_engine.py         # Risk stratification
├── models/                     # Trained model files (.pkl)
├── notebooks/                  # Google Colab training notebooks
│   ├── 01_diabetes_eda.ipynb
│   ├── 02_heart_eda.ipynb
│   ├── 03_ckd_eda.ipynb
│   ├── 04_diabetes_training.ipynb
│   ├── 05_heart_training.ipynb
│   └── 06_ckd_training.ipynb
├── data/sample/               # Test CSV files
└── tests/                     # Unit tests
```

## 🧠 ML Pipeline

### 1. Data Preprocessing
- Automated missing value imputation
- Outlier detection and handling
- Feature scaling and encoding
- Biological impossibility checks (e.g., zero glucose)

### 2. Model Training (PyCaret)
```python
# 5-step AutoML pipeline
setup()           # Configure experiment
compare_models()  # Test 15+ algorithms
tune_model()      # Hyperparameter optimization
evaluate_model()  # Performance metrics
save_model()      # Serialize for deployment
```

### 3. Risk Stratification
- **Low Risk**: Probability < 35%
- **Medium Risk**: Probability 35-65%
- **High Risk**: Probability ≥ 65%

### 4. Explainability (SHAP)
- Waterfall charts showing feature contributions
- Global feature importance rankings
- Plain-language clinical explanations

## 📊 Model Performance Targets

All models trained to achieve:
- **AUC-ROC** ≥ 0.85
- **Accuracy** ≥ 0.80
- **F1 Score** ≥ 0.80

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| AutoML | PyCaret 3.3.2 |
| Explainability | SHAP 0.45.1 |
| Web Framework | Streamlit 1.32.0 |
| Data Processing | Pandas, NumPy |
| ML Library | Scikit-learn 1.4.1 |
| Visualization | Matplotlib, Plotly |
| Optimization | Optuna 3.5.0 |

## 📚 Training Models

### Step 1: Download Datasets
- **Diabetes**: [Kaggle PIMA Indians](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Heart Disease**: [UCI ML Repo](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- **CKD**: [UCI ML Repo](https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease)

### Step 2: Run Training Notebooks
1. Open notebooks in Google Colab
2. Mount Google Drive
3. Upload datasets
4. Run all cells
5. Download trained `.pkl` files to `models/` directory

### Step 3: Test Locally
```bash
streamlit run app.py
```

## 🎨 UI Screenshots

### Patient Input
- CSV batch upload
- Manual form entry with sliders and dropdowns

### Risk Dashboard
- Color-coded risk tiers
- High-risk alert banners
- Clinical recommendations
- Batch results table

### SHAP Explainer
- Waterfall charts
- Feature importance rankings
- Plain-language explanations

## 🧪 Testing

Run unit tests:
```bash
python tests/test_data_processor.py
python tests/test_risk_engine.py
```

## 🚢 Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy with one click

### Local Deployment
```bash
streamlit run app.py --server.port 8501
```

## ⚠️ Clinical Disclaimer

**This tool is for informational and educational purposes only.**

- NOT a diagnostic device
- NOT a substitute for professional medical advice
- Predictions should be validated by licensed healthcare professionals
- Always consult a physician for medical diagnosis and treatment

The platform is intended as a clinical decision support tool to assist healthcare professionals, not replace them.

## 📄 License

MIT License - Open source for educational and research purposes

## 🙏 Acknowledgments

- UCI Machine Learning Repository for datasets
- PyCaret team for AutoML framework
- SHAP library for explainability tools
- Streamlit for rapid prototyping framework

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check documentation in `docs/` folder
- Review training notebooks for examples

## 🗺️ Development Roadmap

### ✅ Phase 1: Project Setup (Complete)
- Repository structure
- Environment configuration
- Dependencies

### ✅ Phase 2: Data Collection & Preprocessing (Complete)
- EDA notebooks
- Data processor module
- Test datasets

### ✅ Phase 3: ML Training (Complete)
- PyCaret training notebooks
- Predictor module
- Risk engine
- SHAP integration

### ✅ Phase 4: Streamlit Dashboard (Complete)
- 5-page web interface
- Custom CSS theme
- CSV upload & manual entry
- Risk visualization

### 🔄 Phase 5: Deployment & Testing (In Progress)
- Model training in Colab
- End-to-end testing
- Streamlit Cloud deployment

### 🔮 Future Enhancements (v2.0)
- LLM-generated clinical recommendations
- Patient history trending over time
- Additional disease modules (liver, stroke, hypertension)
- User authentication
- PDF report export
- Mobile application

---

**Built with ❤️ using Python & Streamlit**

*Healthcare Analytics Platform v1.0*
