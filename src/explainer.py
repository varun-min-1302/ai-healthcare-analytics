"""
Explainability Module
Generates SHAP-based explanations for model predictions
"""

import shap
import matplotlib.pyplot as plt
import pandas as pd
from typing import Any, Optional


class ModelExplainer:
    """Handles SHAP-based model explanations and visualizations"""
    
    def __init__(self):
        self.explainers = {}
        self.shap_values = {}
    
    def create_explainer(self, model: Any, background_data: pd.DataFrame, model_type: str = "tree"):
        """Create SHAP explainer for a given model"""
        try:
            if model_type == "tree":
                explainer = shap.TreeExplainer(model)
            elif model_type == "linear":
                explainer = shap.LinearExplainer(model, background_data)
            else:
                explainer = shap.Explainer(model, background_data)
            
            return explainer
        except Exception as e:
            raise RuntimeError(f"Error creating SHAP explainer: {str(e)}")
    
    def explain_prediction(self, explainer: Any, patient_data: pd.DataFrame):
        """Generate SHAP values for a single prediction"""
        try:
            shap_values = explainer(patient_data)
            return shap_values
        except Exception as e:
            raise RuntimeError(f"Error generating SHAP values: {str(e)}")
    
    def plot_waterfall(self, shap_values, max_display: int = 10):
        """Generate SHAP waterfall plot"""
        fig, ax = plt.subplots(figsize=(10, 6))
        shap.plots.waterfall(shap_values[0], max_display=max_display, show=False)
        plt.tight_layout()
        return fig
    
    def plot_bar(self, shap_values, max_display: int = 10):
        """Generate SHAP bar plot for feature importance"""
        fig, ax = plt.subplots(figsize=(10, 6))
        shap.plots.bar(shap_values[0], max_display=max_display, show=False)
        plt.tight_layout()
        return fig
    
    def get_top_features(self, shap_values, n: int = 3) -> list:
        """Extract top N contributing features from SHAP values"""
        try:
            values = shap_values.values[0]
            features = shap_values.feature_names
            
            # Get absolute values and sort
            abs_values = abs(values)
            top_indices = abs_values.argsort()[-n:][::-1]
            
            top_features = [
                {
                    "feature": features[i],
                    "impact": float(values[i]),
                    "abs_impact": float(abs_values[i])
                }
                for i in top_indices
            ]
            
            return top_features
        except Exception as e:
            return []
    
    def generate_explanation_text(self, top_features: list, disease: str) -> str:
        """Generate plain-language explanation from top features"""
        if not top_features:
            return "Unable to generate explanation."
        
        feature_names = [f["feature"] for f in top_features[:3]]
        explanation = f"The primary risk drivers for {disease} are: {', '.join(feature_names)}."
        
        return explanation
