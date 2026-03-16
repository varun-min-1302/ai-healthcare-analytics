"""
AI-Driven Healthcare Analytics Platform
Main Streamlit Application Entry Point
"""

import streamlit as st
from pathlib import Path
import sys

# Add src to path
sys.path.append(str(Path(__file__).parent))

# Page configuration
st.set_page_config(
    page_title='HealthAI — Multi-Disease Risk Prediction',
    page_icon='🏥',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS for modern healthcare theme
st.markdown('''
<style>
/* ─── Sidebar ─────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: #0D1117;
    border-right: 1px solid #1E2530;
}

/* ─── Metric cards ─────────────────────────────────── */
[data-testid="metric-container"] {
    background: #1A1D27;
    border: 1px solid #252B3B;
    border-radius: 12px;
    padding: 1rem;
}

/* ─── Primary button ───────────────────────────────── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #00C2A0, #0098A0);
    border: none;
    color: white;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5rem 1.5rem;
    transition: transform 0.15s, box-shadow 0.15s;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(0, 194, 160, 0.4);
}

/* ─── Progress bar ─────────────────────────────────── */
.stProgress > div > div {
    background: linear-gradient(90deg, #00C2A0, #5B8FFF);
    border-radius: 4px;
}

/* ─── Alert boxes ─────────────────────────────────── */
.stAlert {
    border-radius: 8px;
    border-left: 4px solid;
}

/* ─── Headers ─────────────────────────────────────── */
h1 {
    color: #E8EAF0;
    font-weight: 700;
}

h2, h3 {
    color: #C9D1D9;
}

/* ─── Tabs ─────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px 8px 0 0;
    padding: 10px 20px;
}
</style>
''', unsafe_allow_html=True)

# Load models at startup
@st.cache_resource
def load_models():
    """Load all disease prediction models (cached)"""
    from src.predictor import DiseasePredictor
    predictor = DiseasePredictor()
    loaded = predictor.load_all_models()
    return predictor, loaded

try:
    predictor, loaded_models = load_models()
    models_available = len(loaded_models) > 0
except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    predictor = None
    models_available = False
    loaded_models = []

# Sidebar navigation
with st.sidebar:
    st.markdown("# 🏥 HealthAI")
    st.markdown("### Multi-Disease Risk Prediction")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ['🏠 Patient Input', '📊 Risk Dashboard', '🧠 SHAP Explainer', 
         '📈 Model Performance', 'ℹ️ About'],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Model status
    if models_available:
        st.success(f"✓ {len(loaded_models)} models loaded")
        for model in loaded_models:
            st.caption(f"• {model.title()}")
    else:
        st.warning("⚠️ No models loaded")
        st.caption("Train models first (Phase 3)")
    
    st.markdown("---")
    st.caption("Healthcare Analytics Platform v1.0")

# Route to pages
if '🏠' in page or 'Input' in page:
    import pages.input_page as p
    p.show(predictor, models_available)
elif '📊' in page or 'Dashboard' in page:
    import pages.dashboard as p
    p.show(predictor)
elif '🧠' in page or 'SHAP' in page:
    import pages.explainer as p
    p.show(predictor)
elif '📈' in page or 'Performance' in page:
    import pages.performance as p
    p.show(predictor, loaded_models)
else:  # About
    import pages.about as p
    p.show()
