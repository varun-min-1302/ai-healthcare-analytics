# 🎨 Application Preview Guide

## How to Launch the Application

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit 1.32.0
- PyCaret 3.3.2
- SHAP 0.45.1
- Pandas, NumPy, Scikit-learn
- Matplotlib, Plotly
- And all other dependencies

### Step 2: Launch the App

```bash
streamlit run app.py
```

The application will automatically open in your browser at:
```
http://localhost:8501
```

---

## 🖼️ What You'll See

### 1. **Home Screen - Patient Input Page** 🏠

**Sidebar Navigation:**
- 🏥 HealthAI logo
- Multi-Disease Risk Prediction subtitle
- Navigation radio buttons (5 pages)
- Model status indicator
- Version info

**Main Content:**
- Title: "Patient Health Input"
- Two tabs:
  - **📁 Upload CSV**: Batch patient processing
  - **✏️ Manual Entry**: Interactive forms

**CSV Upload Tab:**
- Disease selector dropdown (Diabetes/Heart/CKD)
- File uploader widget
- Preview of uploaded data
- "Run Batch Prediction" button (primary style, teal gradient)

**Manual Entry Tab:**
- Disease-specific forms with:
  - **Diabetes**: 8 input fields (sliders, number inputs)
    - Pregnancies, Glucose, Blood Pressure, Skin Thickness
    - Insulin, BMI, Diabetes Pedigree Function, Age
  - **Heart Disease**: 13 input fields
    - Age, Sex, Chest Pain Type, Blood Pressure, Cholesterol
    - Fasting Blood Sugar, ECG, Max Heart Rate, etc.
  - **CKD**: 10 simplified fields
    - Age, BP, Specific Gravity, Albumin, Sugar
    - Blood Glucose, Blood Urea, Creatinine, Hemoglobin, Hypertension
- "Analyze Risk" button (primary style)

---

### 2. **Risk Dashboard** 📊

**Without Results:**
- Info message: "Run a prediction first → Patient Input"
- Instructions on how to use the app

**With Single Patient Results:**
- Alert banner (color-coded by risk):
  - 🟢 **Low Risk**: Green success banner
  - 🟡 **Medium Risk**: Amber warning banner
  - 🔴 **High Risk**: Red error banner with ⚠️
- Three metric cards:
  - Disease name
  - Risk probability (percentage)
  - Risk tier badge
- Progress bar showing probability
- Clinical recommendation box (info style)

**With Batch Results:**
- Summary statistics (4 columns):
  - Total Patients
  - High Risk count
  - Medium Risk count
  - Low Risk count
- Results table with color-coded rows:
  - Patient ID
  - Disease
  - Probability
  - Risk Tier (colored background)
- Download CSV button

---

### 3. **SHAP Explainer** 🧠

**Educational Content:**
- Title: "SHAP Explainer"
- Subtitle: "Understand what drives each prediction"
- What is SHAP? section
- Waterfall Charts explanation
- Feature Importance description

**With Results (when models loaded):**
- SHAP waterfall chart visualization
- Top 3 contributing features
- Feature importance bar chart
- Plain-language explanation

**Placeholder (without models):**
- Warning: "SHAP visualization requires trained models"
- Info: "Feature will be functional once models are trained"

---

### 4. **Model Performance** 📈

**Disease Selector:**
- Dropdown to choose disease module

**Performance Metrics (5 columns):**
- Accuracy: 0.850
- AUC-ROC: 0.875
- F1 Score: 0.832
- Precision: 0.845
- Recall: 0.820

**Model Information (2 columns):**
- Dataset name and source
- Number of features
- Training samples
- Algorithm used
- Target variable
- Class balance

**Training Configuration:**
- Code block showing PyCaret setup
- Normalization, cross-validation, optimization details

**Placeholders:**
- Confusion matrix section
- Global feature importance section
- Note: "Metrics shown are placeholders"

---

### 5. **About Page** ℹ️

**Project Overview:**
- Title: "About HealthAI Platform"
- AI-Driven Healthcare Analytics description

**Supported Disease Modules:**
- Type 2 Diabetes
- Heart Disease
- Chronic Kidney Disease

**Technology Stack:**
- AutoML: PyCaret 3.3.2
- Explainability: SHAP
- Web Framework: Streamlit
- Data Processing: Pandas, NumPy, Scikit-learn
- Visualization: Matplotlib, Plotly

**Features List:**
- Multi-disease risk prediction
- SHAP-based explanations
- Risk stratification
- Automated alerts
- Batch CSV processing
- Manual data entry
- Model performance metrics

**Methodology:**
- 5-step process explanation
- Data preprocessing
- Model training
- Hyperparameter tuning
- Explainability
- Risk stratification

**Model Performance Targets:**
- AUC-ROC ≥ 0.85
- Accuracy ≥ 0.80
- F1 Score ≥ 0.80

**Datasets:**
- UCI Machine Learning Repository
- Kaggle Datasets
- No real patient data used

**Clinical Disclaimer (prominent red box):**
- ⚠️ Warning icon
- "This tool is for informational and educational purposes only"
- "NOT a diagnostic device"
- "NOT a substitute for professional medical advice"
- "Always consult a physician"

**Project Information:**
- Version: 1.0 (MVP)
- Development Timeline: 8 weeks
- Architecture: Modular Python with Streamlit
- Repository structure
- License: MIT
- Acknowledgments

---

## 🎨 Visual Design

### Color Scheme (Dark Healthcare Theme)
- **Primary**: #00C2A0 (Teal) - Buttons, accents
- **Background**: #0F1117 (Dark) - Main background
- **Secondary**: #1A1D27 (Darker) - Cards, panels
- **Text**: #E8EAF0 (Light) - Primary text
- **Success**: #00C2A0 (Green) - Low risk
- **Warning**: #FFB547 (Amber) - Medium risk
- **Error**: #FF6B6B (Red) - High risk

### UI Components

**Buttons:**
- Primary: Teal gradient with hover effect
- Rounded corners (8px)
- Shadow on hover
- Smooth transitions

**Metric Cards:**
- Dark background (#1A1D27)
- Border (#252B3B)
- Rounded corners (12px)
- Padding for spacing

**Progress Bars:**
- Teal to blue gradient
- Rounded (4px)
- Smooth animation

**Alert Boxes:**
- Rounded corners (8px)
- Left border accent (4px)
- Color-coded by severity

**Tabs:**
- Rounded top corners
- Gap between tabs
- Active tab highlighted

### Typography
- **Headers**: Bold, high contrast (#E8EAF0)
- **Body**: Regular, readable (#C9D1D9)
- **Captions**: Muted, smaller (#8B949E)
- **Font**: Sans-serif

---

## 🖱️ Interactive Elements

### Sidebar
- Fixed left panel
- Dark background (#0D1117)
- Navigation radio buttons
- Model status indicator
- Collapsible on mobile

### Forms
- **Sliders**: Interactive with value display
- **Number Inputs**: Keyboard entry
- **Dropdowns**: Searchable select boxes
- **File Upload**: Drag & drop support

### Feedback
- **Loading Spinners**: During processing
- **Progress Bars**: For batch operations
- **Success Messages**: Green checkmark
- **Error Messages**: Red with icon
- **Info Messages**: Blue with icon

---

## 📱 Responsive Design

### Desktop (> 1024px)
- Wide layout
- 3-column forms
- Full sidebar visible
- Large metric cards

### Tablet (768px - 1024px)
- 2-column forms
- Collapsible sidebar
- Stacked metrics

### Mobile (< 768px)
- Single column layout
- Hamburger menu
- Vertical stacking
- Touch-friendly buttons

---

## 🎭 User Experience Flow

### First-Time User
1. Lands on Patient Input page
2. Sees "Models not loaded" warning
3. Can explore UI and forms
4. Reads About page for context
5. Understands educational purpose

### With Trained Models
1. Uploads CSV or enters data manually
2. Clicks "Analyze Risk"
3. Sees loading spinner
4. Redirected to Risk Dashboard
5. Views color-coded results
6. Checks SHAP explanations
7. Downloads results (if batch)

### Error Scenarios
1. Invalid CSV → Clear error message
2. Missing columns → List of required columns
3. Model not loaded → Instructions to train
4. Processing error → User-friendly message

---

## 🎬 Demo Scenarios

### Scenario 1: Single Patient (Low Risk)
```
Input: Glucose=85, BMI=22, Age=25
Result: 25% probability → Low Risk (Green)
Alert: None
Recommendation: Continue regular health monitoring
```

### Scenario 2: Single Patient (High Risk)
```
Input: Glucose=195, BMI=41.5, Age=55
Result: 85% probability → High Risk (Red)
Alert: ⚠️ HIGH RISK detected for Diabetes (85%)
Recommendation: Recommend HbA1c test and dietary consultation
```

### Scenario 3: Batch Upload
```
Upload: diabetes_test.csv (5 patients)
Processing: Progress bar 0% → 100%
Result: 2 Low, 1 Medium, 2 High
Alert: ⚠️ 2 HIGH RISK patients detected
Download: CSV with all results
```

---

## 🔧 Testing the Preview

### Quick Test Checklist
- [ ] App launches without errors
- [ ] All 5 pages load
- [ ] Navigation works
- [ ] Forms accept input
- [ ] CSV upload works
- [ ] Error messages clear
- [ ] Disclaimer visible
- [ ] Theme renders correctly
- [ ] Mobile responsive

### Sample Data
Use files in `data/sample/`:
- `diabetes_test.csv` - 5 diabetes patients
- `heart_test.csv` - 5 heart disease patients
- `ckd_test.csv` - 5 CKD patients

---

## 📸 Screenshots (To Be Added)

After launching, take screenshots of:
1. Home page with forms
2. Risk dashboard with results
3. SHAP explainer page
4. Model performance page
5. About page with disclaimer

Add to README.md for marketing.

---

## 🚀 Next Steps After Preview

1. **Test thoroughly** - Try all features
2. **Check mobile** - Test on phone/tablet
3. **Review UI** - Note any improvements
4. **Train models** - For full functionality
5. **Deploy** - Push to Streamlit Cloud

---

**Ready to preview?** Run `streamlit run app.py` and explore! 🎉
