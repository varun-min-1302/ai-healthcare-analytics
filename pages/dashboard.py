"""
Risk Dashboard Page
Display prediction results with risk tiers and alerts
"""

import streamlit as st
import pandas as pd


def show(predictor):
    """Display risk dashboard"""
    st.title('📊 Risk Dashboard')
    
    # Check for results
    has_batch = 'batch_results' in st.session_state
    has_single = 'single_result' in st.session_state
    
    if not has_batch and not has_single:
        st.info('👈 Run a prediction first in Patient Input page')
        st.markdown("""
        ### How to use:
        1. Go to **Patient Input** page
        2. Upload CSV or enter patient data manually
        3. Click **Analyze Risk**
        4. Return here to view results
        """)
        return
    
    # Display single result
    if has_single:
        st.subheader("Individual Patient Analysis")
        result = st.session_state['single_result']
        disease = st.session_state.get('disease', 'unknown')
        
        display_single_result(result, disease)
    
    # Display batch results
    if has_batch:
        st.subheader("Batch Analysis Results")
        results = st.session_state['batch_results']
        disease = st.session_state.get('disease', 'unknown')
        
        display_batch_results(results, disease)


def display_single_result(result, disease):
    """Display single patient risk assessment"""
    prob = result['probability']
    tier = result['risk_tier']
    
    # High-risk alert banner
    if tier == 'High':
        st.error(f"⚠️ **HIGH RISK** detected for {disease.title()} ({prob:.1%})")
    elif tier == 'Medium':
        st.warning(f"⚡ **MEDIUM RISK** for {disease.title()} ({prob:.1%})")
    else:
        st.success(f"✓ **LOW RISK** for {disease.title()} ({prob:.1%})")
    
    # Risk metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Disease",
            disease.title(),
            delta=None
        )
    
    with col2:
        st.metric(
            "Risk Probability",
            f"{prob:.1%}",
            delta=tier
        )
    
    with col3:
        color = get_tier_color(tier)
        st.markdown(f"""
        <div style='padding: 1rem; background: {color}20; border-radius: 8px; text-align: center;'>
            <h3 style='margin: 0; color: {color};'>{tier} Risk</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress bar
    st.progress(prob)
    
    # Clinical recommendation
    st.markdown("### 📋 Clinical Recommendation")
    recommendation = get_recommendation(disease, tier)
    st.info(recommendation)


def display_batch_results(results, disease):
    """Display batch prediction results"""
    # Summary statistics
    total = len(results)
    high_risk = sum(1 for r in results if r['risk_tier'] == 'High')
    medium_risk = sum(1 for r in results if r['risk_tier'] == 'Medium')
    low_risk = sum(1 for r in results if r['risk_tier'] == 'Low')
    
    # Alert for high-risk patients
    if high_risk > 0:
        st.error(f"⚠️ {high_risk} HIGH RISK patients detected out of {total}")
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Patients", total)
    with col2:
        st.metric("High Risk", high_risk, delta="Critical" if high_risk > 0 else None)
    with col3:
        st.metric("Medium Risk", medium_risk)
    with col4:
        st.metric("Low Risk", low_risk)
    
    # Results table
    st.markdown("### Patient Risk Summary")
    
    df_results = pd.DataFrame(results)
    df_results['probability'] = df_results['probability'].apply(lambda x: f"{x:.1%}")
    
    # Color code by risk tier
    def color_risk(val):
        if val == 'High':
            return 'background-color: #FF6B6B40'
        elif val == 'Medium':
            return 'background-color: #FFB54740'
        else:
            return 'background-color: #00C2A040'
    
    styled_df = df_results.style.applymap(color_risk, subset=['risk_tier'])
    st.dataframe(styled_df, use_container_width=True)
    
    # Download results
    csv = df_results.to_csv(index=False)
    st.download_button(
        label="📥 Download Results CSV",
        data=csv,
        file_name=f"{disease}_risk_assessment.csv",
        mime="text/csv"
    )


def get_tier_color(tier):
    """Get color for risk tier"""
    colors = {
        'Low': '#00C2A0',
        'Medium': '#FFB547',
        'High': '#FF6B6B'
    }
    return colors.get(tier, '#888888')


def get_recommendation(disease, tier):
    """Get clinical recommendation"""
    recommendations = {
        'diabetes': {
            'High': '🔴 Recommend HbA1c confirmatory test and dietary consultation. Consider immediate endocrinology referral.',
            'Medium': '🟡 Monitor glucose levels closely. Consider lifestyle modifications and follow-up in 3 months.',
            'Low': '🟢 Continue regular health monitoring. Maintain healthy lifestyle habits.'
        },
        'heart': {
            'High': '🔴 Recommend ECG, lipid panel, and cardiology referral. Consider stress test.',
            'Medium': '🟡 Monitor blood pressure and cholesterol levels. Follow-up in 6 months.',
            'Low': '🟢 Maintain healthy lifestyle and regular checkups.'
        },
        'ckd': {
            'High': '🔴 Recommend serum creatinine test and nephrology consultation. Monitor kidney function closely.',
            'Medium': '🟡 Monitor kidney function and blood pressure. Follow-up in 3-6 months.',
            'Low': '🟢 Continue routine health monitoring.'
        }
    }
    
    return recommendations.get(disease, {}).get(tier, 'Consult healthcare provider for further evaluation.')
