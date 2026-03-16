"""
SHAP Explainer Page
Display SHAP visualizations and feature importance
"""

import streamlit as st


def show(predictor):
    """Display SHAP explainer page"""
    st.title('🧠 SHAP Explainer')
    st.markdown("Understand what drives each prediction using SHAP (SHapley Additive exPlanations)")
    
    # Check for results
    has_result = 'single_result' in st.session_state or 'batch_results' in st.session_state
    
    if not has_result:
        st.info('👈 Run a prediction first in Patient Input page')
        
        # Educational content
        st.markdown("""
        ### What is SHAP?
        
        SHAP (SHapley Additive exPlanations) is a game-theoretic approach to explain 
        machine learning predictions. It shows:
        
        - **Which features** contributed most to the prediction
        - **How much** each feature influenced the result
        - **Direction** of influence (increasing or decreasing risk)
        
        ### Waterfall Charts
        
        SHAP waterfall charts visualize:
        - Base value (average model output)
        - How each feature pushes the prediction higher or lower
        - Final prediction value
        
        ### Feature Importance
        
        Global feature importance shows which features are most influential 
        across all predictions in the training dataset.
        """)
        
        return
    
    st.warning("⚠️ SHAP visualization requires trained models with explainer integration")
    st.info("This feature will be fully functional once models are trained in Phase 3")
    
    # Placeholder for SHAP visualizations
    st.markdown("### 📊 SHAP Waterfall Chart")
    st.markdown("*Waterfall chart will appear here showing feature contributions*")
    
    st.markdown("### 📈 Feature Importance")
    st.markdown("*Global feature importance bar chart will appear here*")
    
    # Example explanation
    if 'single_result' in st.session_state:
        result = st.session_state['single_result']
        disease = st.session_state.get('disease', 'unknown')
        
        st.markdown("### 🔍 Prediction Explanation")
        st.markdown(f"""
        For this {disease.title()} prediction:
        - **Risk Probability:** {result['probability']:.1%}
        - **Risk Tier:** {result['risk_tier']}
        
        *Top contributing features will be displayed here once SHAP integration is complete*
        """)
