"""
Model Performance Page
Display model metrics and evaluation results
"""

import streamlit as st
import pandas as pd


def show(predictor, loaded_models):
    """Display model performance page"""
    st.title('📈 Model Performance')
    st.markdown("View training metrics and evaluation results for each disease module")
    
    if not loaded_models:
        st.warning("⚠️ No models loaded. Train models first (Phase 3)")
        return
    
    # Disease selector
    disease = st.selectbox(
        'Select Disease Module',
        loaded_models,
        format_func=lambda x: x.title()
    )
    
    st.markdown(f"## {disease.title()} Model")
    
    # Placeholder metrics (will be populated from actual model evaluation)
    st.markdown("### 📊 Performance Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Accuracy", "0.850", help="Overall prediction accuracy")
    with col2:
        st.metric("AUC-ROC", "0.875", help="Area under ROC curve")
    with col3:
        st.metric("F1 Score", "0.832", help="Harmonic mean of precision and recall")
    with col4:
        st.metric("Precision", "0.845", help="True positives / (True positives + False positives)")
    with col5:
        st.metric("Recall", "0.820", help="True positives / (True positives + False negatives)")
    
    st.info("📝 Note: Metrics shown are placeholders. Actual metrics will be loaded from trained models.")
    
    # Model information
    st.markdown("### ℹ️ Model Information")
    
    model_info = get_model_info(disease)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Dataset:**")
        st.write(model_info['dataset'])
        
        st.markdown("**Features:**")
        st.write(model_info['n_features'])
        
        st.markdown("**Training Samples:**")
        st.write(model_info['n_samples'])
    
    with col2:
        st.markdown("**Algorithm:**")
        st.write(model_info['algorithm'])
        
        st.markdown("**Target:**")
        st.write(model_info['target'])
        
        st.markdown("**Class Balance:**")
        st.write(model_info['class_balance'])
    
    # Training details
    st.markdown("### 🔧 Training Configuration")
    
    st.code(f"""
PyCaret Setup:
- Normalization: True
- Cross-validation: 5-fold
- Optimization metric: AUC-ROC
- Hyperparameter tuning: Optuna (50 iterations)
- Class imbalance handling: {model_info['imbalance_handling']}
    """, language="yaml")
    
    # Confusion matrix placeholder
    st.markdown("### 📉 Confusion Matrix")
    st.info("Confusion matrix visualization will appear here once models are trained")
    
    # Feature importance placeholder
    st.markdown("### 🎯 Global Feature Importance")
    st.info("SHAP-based global feature importance will appear here")


def get_model_info(disease):
    """Get model information"""
    info = {
        'diabetes': {
            'dataset': 'PIMA Indians Diabetes',
            'n_features': 8,
            'n_samples': '768 (train: 614, test: 154)',
            'algorithm': 'TBD (AutoML selection)',
            'target': 'Outcome (0/1)',
            'class_balance': '~65% negative, ~35% positive',
            'imbalance_handling': 'SMOTE'
        },
        'heart': {
            'dataset': 'Cleveland Heart Disease',
            'n_features': 13,
            'n_samples': '303 (train: 242, test: 61)',
            'algorithm': 'TBD (AutoML selection)',
            'target': 'target (0/1)',
            'class_balance': '~54% negative, ~46% positive',
            'imbalance_handling': 'None (balanced)'
        },
        'ckd': {
            'dataset': 'Chronic Kidney Disease',
            'n_features': 24,
            'n_samples': '400 (train: 320, test: 80)',
            'algorithm': 'TBD (AutoML selection)',
            'target': 'classification (ckd/notckd)',
            'class_balance': '~62% CKD, ~38% not CKD',
            'imbalance_handling': 'SMOTE'
        }
    }
    
    return info.get(disease, {})
