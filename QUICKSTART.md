# 🚀 Quick Start Guide

Get the Healthcare Analytics Platform running in 5 minutes!

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional)

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Streamlit (web framework)
- PyCaret (AutoML)
- SHAP (explainability)
- Pandas, NumPy, Scikit-learn
- Matplotlib, Plotly

### 2. Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## First Steps

### Without Trained Models

The app will run but show warnings that models aren't loaded. You can:

1. **Explore the UI** - Navigate through all 5 pages
2. **Test Forms** - Try the manual data entry forms
3. **View Documentation** - Read the About page
4. **Check Structure** - See how the app is organized

### With Trained Models

Once you have trained models (see below), you can:

1. **Upload CSV** - Go to Patient Input → Upload CSV tab
2. **Use Sample Data** - Upload `data/sample/diabetes_test.csv`
3. **View Results** - Navigate to Risk Dashboard
4. **See Explanations** - Check SHAP Explainer page

## Training Models (Required for Full Functionality)

### Option 1: Google Colab (Recommended)

1. Open `notebooks/04_diabetes_training.ipynb` in Google Colab
2. Click "Runtime" → "Run all"
3. Download the generated `diabetes_model.pkl`
4. Place it in the `models/` directory
5. Repeat for heart and CKD models

### Option 2: Local Training

```bash
# Install additional dependencies
pip install pycaret[full]

# Run training script (create this based on notebooks)
python scripts/train_models.py
```

## Testing the App

### Test with Sample Data

```bash
# The app is running at http://localhost:8501

1. Go to "Patient Input" page
2. Select "Diabetes" from dropdown
3. Click "Upload CSV" tab
4. Upload: data/sample/diabetes_test.csv
5. Click "Run Batch Prediction"
6. Go to "Risk Dashboard" to see results
```

### Test Manual Entry

```bash
1. Go to "Patient Input" page
2. Click "Manual Entry" tab
3. Select "Diabetes"
4. Adjust sliders (try: Glucose=195, BMI=41, Age=55)
5. Click "Analyze Risk"
6. Go to "Risk Dashboard"
```

## Troubleshooting

### "No models loaded" warning

**Solution**: Train models using notebooks in Google Colab, then place .pkl files in `models/` directory

### Import errors

**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

### Port already in use

**Solution**: Use a different port
```bash
streamlit run app.py --server.port 8502
```

### Streamlit not found

**Solution**: Ensure pip installation was successful
```bash
pip install streamlit
streamlit --version
```

## Project Structure

```
healthai-platform/
├── app.py              # ← Start here
├── pages/              # Dashboard pages
├── src/                # Core modules
├── models/             # Place trained .pkl files here
├── data/sample/        # Test CSV files
└── notebooks/          # Training notebooks (use in Colab)
```

## Next Steps

1. ✅ App running locally
2. ⏳ Train models in Google Colab
3. ⏳ Test with sample data
4. ⏳ Deploy to Streamlit Cloud

## Deployment to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository
5. Set main file: `app.py`
6. Click "Deploy"

## Getting Help

- **Documentation**: Check `docs/` folder
- **Examples**: See `notebooks/` for training examples
- **Issues**: Open an issue on GitHub
- **Tests**: Run `python tests/test_risk_engine.py`

## Quick Commands

```bash
# Run app
streamlit run app.py

# Run tests
python tests/test_data_processor.py
python tests/test_risk_engine.py

# Generate test data
python scripts/generate_test_data.py

# Check dependencies
pip list | grep -E "streamlit|pycaret|shap"
```

## Success Checklist

- [ ] Dependencies installed
- [ ] App launches without errors
- [ ] All 5 pages accessible
- [ ] Forms accept input
- [ ] Sample CSV uploads successfully
- [ ] Models trained (optional for UI testing)
- [ ] Predictions working (requires models)

---

**You're all set!** 🎉

For detailed information, see the main [README.md](README.md)
