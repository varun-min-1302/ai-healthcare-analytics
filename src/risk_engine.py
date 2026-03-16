"""
Risk Assessment Engine
Applies risk stratification logic and generates alerts
"""

from dataclasses import dataclass
from typing import Literal, List
import numpy as np


# Risk tier thresholds
THRESHOLDS = {
    'low_max': 0.35,
    'high_min': 0.65
}


@dataclass
class RiskResult:
    """Structured risk assessment result"""
    disease: str
    probability: float
    tier: Literal['Low', 'Medium', 'High']
    color: str
    alert: bool
    top_factors: List[str]
    recommendation: str = ""


def classify_risk(disease: str, probability: float, 
                 shap_values, feature_names: list) -> RiskResult:
    """
    Classify disease risk into Low/Medium/High tiers
    
    Args:
        disease: Disease name (diabetes, heart, ckd)
        probability: Model prediction probability (0-1)
        shap_values: SHAP values from explainer
        feature_names: List of feature names
    
    Returns:
        RiskResult with tier, color, alert flag, and top factors
    """
    p = float(probability)
    
    # Determine risk tier and color
    if p < THRESHOLDS['low_max']:
        tier, color = 'Low', '#00C2A0'
    elif p >= THRESHOLDS['high_min']:
        tier, color = 'High', '#FF6B6B'
    else:
        tier, color = 'Medium', '#FFB547'
    
    # Extract top 3 contributing features from SHAP
    shap_abs = np.abs(shap_values.values[0])
    top_idx = shap_abs.argsort()[-3:][::-1]
    top_factors = [feature_names[i] for i in top_idx]
    
    # Get clinical recommendation
    recommendation = get_recommendation(disease, tier)
    
    return RiskResult(
        disease=disease,
        probability=p,
        tier=tier,
        color=color,
        alert=(tier == 'High'),
        top_factors=top_factors,
        recommendation=recommendation
    )


def get_recommendation(disease: str, tier: str) -> str:
    """Get clinical recommendation based on disease and risk tier"""
    recommendations = {
        'diabetes': {
            'High': 'Recommend HbA1c confirmatory test and dietary consultation.',
            'Medium': 'Monitor glucose levels and consider lifestyle modifications.',
            'Low': 'Continue regular health monitoring.'
        },
        'heart': {
            'High': 'Recommend ECG, lipid panel, and cardiology referral.',
            'Medium': 'Monitor blood pressure and cholesterol levels.',
            'Low': 'Maintain healthy lifestyle and regular checkups.'
        },
        'ckd': {
            'High': 'Recommend serum creatinine test and nephrology consultation.',
            'Medium': 'Monitor kidney function and blood pressure.',
            'Low': 'Continue routine health monitoring.'
        }
    }
    
    return recommendations.get(disease, {}).get(tier, 'Consult healthcare provider.')


def format_alert_message(risk: RiskResult) -> str:
    """Format alert message for high-risk predictions"""
    if not risk.alert:
        return ""
    
    factors_str = ", ".join(risk.top_factors)
    return (f"⚠️ HIGH RISK detected for {risk.disease.title()} "
            f"({risk.probability:.1%}). "
            f"Primary factors: {factors_str}")
