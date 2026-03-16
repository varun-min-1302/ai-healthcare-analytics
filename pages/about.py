"""
About Page
Project information and disclaimer
"""

import streamlit as st


def show():
    """Display about page"""
    st.title('ℹ️ About HealthAI Platform')
    
    st.markdown("""
    ## AI-Driven Healthcare Analytics
    
    This platform leverages machine learning and explainable AI (XAI) to predict 
    multi-disease risk from patient health data.
    
    ### 🎯 Supported Disease Modules
    
    - **Type 2 Diabetes** - PIMA Indians Diabetes Dataset
    - **Heart Disease** - Cleveland Heart Disease Dataset
    - **Chronic Kidney Disease** - CKD Dataset
    
    ### 🛠️ Technology Stack
    
    - **AutoML**: PyCaret 3.3.2 for automated model selection and training
    - **Explainability**: SHAP for interpretable predictions
    - **Web Framework**: Streamlit for interactive dashboard
    - **Data Processing**: Pandas, NumPy, Scikit-learn
    - **Visualization**: Matplotlib, Plotly
    
    ### 📊 Features
    
    - ✅ Multi-disease risk prediction
    - ✅ SHAP-based prediction explanations
    - ✅ Risk stratification (Low/Medium/High)
    - ✅ Automated alert system for high-risk cases
    - ✅ Batch CSV processing
    - ✅ Manual patient data entry
    - ✅ Model performance metrics
    
    ### 🔬 Methodology
    
    1. **Data Preprocessing**: Automated handling of missing values, outliers, and feature scaling
    2. **Model Training**: PyCaret AutoML compares 15+ algorithms and selects the best performer
    3. **Hyperparameter Tuning**: Optuna-based optimization for maximum AUC-ROC
    4. **Explainability**: SHAP values show which features drive each prediction
    5. **Risk Stratification**: Probability scores mapped to clinical risk tiers
    
    ### 📈 Model Performance Targets
    
    All models trained to achieve:
    - **AUC-ROC** ≥ 0.85
    - **Accuracy** ≥ 0.80
    - **F1 Score** ≥ 0.80
    
    ### 📚 Datasets
    
    All training data sourced from publicly available repositories:
    - UCI Machine Learning Repository
    - Kaggle Datasets
    
    No real patient data used in development.
    """)
    
    # Disclaimer
    st.markdown("---")
    st.error("""
    ### ⚠️ Clinical Disclaimer
    
    **This tool is for informational and educational purposes only.**
    
    - NOT a diagnostic device
    - NOT a substitute for professional medical advice
    - Predictions should be validated by licensed healthcare professionals
    - Always consult a physician for medical diagnosis and treatment
    
    The platform is intended as a clinical decision support tool to assist 
    healthcare professionals, not replace them.
    """)
    
    # Project info
    st.markdown("---")
    st.markdown("""
    ### 👨‍💻 Project Information
    
    **Version**: 1.0 (MVP)  
    **Development Timeline**: 8 weeks  
    **Architecture**: Modular Python with Streamlit frontend
    
    **Repository Structure**:
    ```
    healthai-platform/
    ├── app.py              # Main application
    ├── pages/              # Dashboard pages
    ├── src/                # Core modules
    ├── models/             # Trained models
    ├── notebooks/          # Training notebooks
    └── tests/              # Unit tests
    ```
    
    ### 📄 License
    
    MIT License - Open source for educational and research purposes
    
    ### 🙏 Acknowledgments
    
    - UCI Machine Learning Repository for datasets
    - PyCaret team for AutoML framework
    - SHAP library for explainability tools
    - Streamlit for rapid prototyping framework
    """)
    
    st.markdown("---")
    st.caption("Healthcare Analytics Platform v1.0 | Built with ❤️ using Python & Streamlit")
