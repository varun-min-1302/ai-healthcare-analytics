"""
Patient Input Page
CSV upload and manual form entry for patient data
"""

import streamlit as st
import pandas as pd
from src.data_processor import DataProcessor, FEATURE_CONFIGS


def show(predictor, models_available):
    """Display patient input page"""
    st.title('🏠 Patient Health Input')
    st.markdown("Enter patient data via CSV upload or manual form entry")
    
    if not models_available:
        st.warning("⚠️ No models loaded. Please train models first (see Phase 3).")
        return
    
    tab1, tab2 = st.tabs(['📁 Upload CSV', '✏️ Manual Entry'])
    
    # Tab 1: CSV Upload
    with tab1:
        st.subheader("Batch Patient Analysis")
        
        disease = st.selectbox(
            'Select Disease Module',
            ['diabetes', 'heart', 'ckd'],
            format_func=lambda x: x.title()
        )
        
        uploaded_file = st.file_uploader(
            'Upload Patient Data CSV',
            type=['csv'],
            help=f"Required columns: {', '.join(FEATURE_CONFIGS[disease]['features'])}"
        )
        
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                st.success(f"✓ Loaded {len(df)} patient records")
                st.dataframe(df.head(), use_container_width=True)
                
                if st.button('▶ Run Batch Prediction', type='primary', key='batch'):
                    with st.spinner('Analyzing patient data...'):
                        results = process_batch(df, disease, predictor)
                        st.session_state['batch_results'] = results
                        st.session_state['disease'] = disease
                        st.success(f'✓ Processed {len(results)} patients. Go to Dashboard →')
                        st.balloons()
            
            except Exception as e:
                st.error(f"Error loading CSV: {str(e)}")
    
    # Tab 2: Manual Entry
    with tab2:
        disease_manual = st.selectbox(
            'Disease Module',
            ['diabetes', 'heart', 'ckd'],
            format_func=lambda x: x.title(),
            key='manual_disease'
        )
        
        if disease_manual == 'diabetes':
            show_diabetes_form(predictor)
        elif disease_manual == 'heart':
            show_heart_form(predictor)
        else:
            show_ckd_form(predictor)


def show_diabetes_form(predictor):
    """Manual form for diabetes risk assessment"""
    st.subheader("Diabetes Risk Screening")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pregnancies = st.number_input('Pregnancies', 0, 20, 1)
        glucose = st.slider('Glucose (mg/dL)', 50, 250, 120)
        bp = st.slider('Blood Pressure (mm Hg)', 40, 130, 72)
    
    with col2:
        skin = st.slider('Skin Thickness (mm)', 0, 100, 20)
        insulin = st.number_input('Insulin (μU/mL)', 0, 900, 80)
        bmi = st.slider('BMI', 15.0, 55.0, 28.0, 0.1)
    
    with col3:
        dpf = st.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.5, 0.01)
        age = st.slider('Age', 18, 90, 35)
    
    if st.button('🔍 Analyze Risk', type='primary', key='diabetes_analyze'):
        patient_data = pd.DataFrame([{
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': bp,
            'SkinThickness': skin,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': dpf,
            'Age': age
        }])
        
        with st.spinner('Analyzing...'):
            result = predictor.predict('diabetes', patient_data)
            st.session_state['single_result'] = result
            st.session_state['disease'] = 'diabetes'
            st.success('✓ Analysis complete! View results in Dashboard →')


def show_heart_form(predictor):
    """Manual form for heart disease risk assessment"""
    st.subheader("Heart Disease Risk Screening")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider('Age', 18, 90, 50)
        sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
        cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
        trestbps = st.slider('Resting Blood Pressure', 90, 200, 120)
        chol = st.slider('Cholesterol (mg/dL)', 100, 400, 200)
    
    with col2:
        fbs = st.selectbox('Fasting Blood Sugar > 120', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        restecg = st.selectbox('Resting ECG', [0, 1, 2])
        thalach = st.slider('Max Heart Rate', 60, 220, 150)
        exang = st.selectbox('Exercise Induced Angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    
    with col3:
        oldpeak = st.slider('ST Depression', 0.0, 6.0, 1.0, 0.1)
        slope = st.selectbox('Slope of Peak Exercise ST', [0, 1, 2])
        ca = st.selectbox('Number of Major Vessels', [0, 1, 2, 3])
        thal = st.selectbox('Thalassemia', [0, 1, 2, 3])
    
    if st.button('🔍 Analyze Risk', type='primary', key='heart_analyze'):
        patient_data = pd.DataFrame([{
            'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps,
            'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalach': thalach,
            'exang': exang, 'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
        }])
        
        with st.spinner('Analyzing...'):
            result = predictor.predict('heart', patient_data)
            st.session_state['single_result'] = result
            st.session_state['disease'] = 'heart'
            st.success('✓ Analysis complete! View results in Dashboard →')


def show_ckd_form(predictor):
    """Manual form for CKD risk assessment"""
    st.subheader("Chronic Kidney Disease Risk Screening")
    st.info("Simplified form - full CKD assessment requires 20+ clinical parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider('Age', 18, 90, 50)
        bp = st.slider('Blood Pressure', 50, 180, 80)
        sg = st.slider('Specific Gravity', 1.005, 1.025, 1.020, 0.005)
        al = st.selectbox('Albumin', [0, 1, 2, 3, 4])
        su = st.selectbox('Sugar', [0, 1, 2, 3, 4])
    
    with col2:
        bgr = st.slider('Blood Glucose Random', 70, 500, 120)
        bu = st.slider('Blood Urea', 10, 200, 40)
        sc = st.slider('Serum Creatinine', 0.5, 15.0, 1.2, 0.1)
        hemo = st.slider('Hemoglobin', 3.0, 18.0, 12.0, 0.1)
        htn = st.selectbox('Hypertension', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    
    st.warning("⚠️ CKD form is simplified. Full implementation requires all 20 features.")


def process_batch(df, disease, predictor):
    """Process batch CSV predictions with progress tracking"""
    processor = DataProcessor()
    
    try:
        # Validate CSV first
        is_valid, message = processor.validate_csv(df, disease)
        if not is_valid:
            st.error(f"❌ CSV Validation Failed: {message}")
            st.info("💡 Download sample CSV template from the sidebar")
            return []
        elif "Extra columns" in message:
            st.warning(message)
        
        # Validate and preprocess
        df_clean = processor.validate_and_preprocess(df, disease)
        
        # Generate predictions with progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        results = []
        total = len(df_clean)
        
        for idx, row in df_clean.iterrows():
            status_text.text(f"Processing patient {idx + 1} of {total}...")
            
            try:
                patient_df = pd.DataFrame([row])
                result = predictor.predict(disease, patient_df)
                result['patient_id'] = idx + 1
                results.append(result)
            except Exception as e:
                st.warning(f"⚠️ Failed to process patient {idx + 1}: {str(e)}")
                continue
            
            progress_bar.progress((idx + 1) / total)
        
        progress_bar.empty()
        status_text.empty()
        
        return results
    
    except ValueError as e:
        st.error(f"❌ Validation Error: {str(e)}")
        st.info("💡 Expected columns: " + ", ".join(FEATURE_CONFIGS[disease]['features']))
        return []
    except Exception as e:
        st.error(f"❌ Error processing batch: {str(e)}")
        st.info("💡 Please check your CSV format and try again")
        return []
