"""
Risk Assessment Engine
Applies risk stratification logic and generates alerts
"""

from typing import Dict, Any, List


class RiskEngine:
    """Handles risk tier classification and alert generation"""
    
    # Risk thresholds
    LOW_THRESHOLD = 0.35
    HIGH_THRESHOLD = 0.65
    
    def __init__(self):
        self.alerts = []
    
    def classify_risk(self, probability: float) -> Dict[str, Any]:
        """Classify risk probability into tier with metadata"""
        if probability < self.LOW_THRESHOLD:
            tier = "Low"
            color = "green"
            severity = 1
        elif probability <= self.HIGH_THRESHOLD:
            tier = "Medium"
            color = "orange"
            severity = 2
        else:
            tier = "High"
            color = "red"
            severity = 3
        
        return {
            "tier": tier,
            "color": color,
            "severity": severity,
            "probability": probability
        }
    
    def generate_alert(self, disease: str, probability: float, top_factors: List[str]) -> Dict[str, Any]:
        """Generate alert for high-risk predictions"""
        risk_info = self.classify_risk(probability)
        
        if risk_info["severity"] == 3:  # High risk
            alert = {
                "disease": disease.title(),
                "probability": f"{probability:.1%}",
                "risk_tier": risk_info["tier"],
                "top_factors": top_factors[:3],
                "message": f"⚠️ HIGH RISK detected for {disease.title()} ({probability:.1%})",
                "recommendation": self._get_recommendation(disease)
            }
            self.alerts.append(alert)
            return alert
        
        return None
    
    def _get_recommendation(self, disease: str) -> str:
        """Get static clinical recommendation based on disease"""
        recommendations = {
            "diabetes": "Recommend HbA1c confirmatory test and dietary consultation.",
            "heart": "Recommend ECG, lipid panel, and cardiology referral.",
            "ckd": "Recommend serum creatinine test and nephrology consultation."
        }
        return recommendations.get(disease, "Consult with healthcare provider for further evaluation.")
    
    def get_all_alerts(self) -> List[Dict[str, Any]]:
        """Retrieve all generated alerts"""
        return self.alerts
    
    def clear_alerts(self):
        """Clear all stored alerts"""
        self.alerts = []
    
    def get_risk_summary(self, predictions: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Generate overall risk summary from multiple disease predictions"""
        total_diseases = len(predictions)
        high_risk_count = sum(1 for p in predictions.values() if p.get("risk_tier") == "High")
        medium_risk_count = sum(1 for p in predictions.values() if p.get("risk_tier") == "Medium")
        
        overall_severity = "Low"
        if high_risk_count > 0:
            overall_severity = "Critical"
        elif medium_risk_count >= 2:
            overall_severity = "Elevated"
        elif medium_risk_count == 1:
            overall_severity = "Moderate"
        
        return {
            "total_diseases_assessed": total_diseases,
            "high_risk_count": high_risk_count,
            "medium_risk_count": medium_risk_count,
            "overall_severity": overall_severity
        }
