"""
Test script for risk_engine module
Validates risk classification and alert generation
"""

import sys
sys.path.append('.')

from src.risk_engine import classify_risk, get_recommendation, format_alert_message, THRESHOLDS
import numpy as np


class MockSHAPValues:
    """Mock SHAP values for testing"""
    def __init__(self, values):
        self.values = np.array([values])


def test_risk_classification():
    """Test risk tier classification"""
    print("Testing Risk Classification...")
    
    # Mock SHAP values
    shap_vals = MockSHAPValues([0.5, 0.3, 0.2, 0.1, 0.05])
    features = ['Glucose', 'BMI', 'Age', 'BloodPressure', 'Insulin']
    
    # Test Low risk
    result_low = classify_risk('diabetes', 0.25, shap_vals, features)
    assert result_low.tier == 'Low'
    assert result_low.color == '#00C2A0'
    assert result_low.alert == False
    print(f"✓ Low risk: {result_low.probability:.1%} -> {result_low.tier}")
    
    # Test Medium risk
    result_med = classify_risk('diabetes', 0.50, shap_vals, features)
    assert result_med.tier == 'Medium'
    assert result_med.color == '#FFB547'
    assert result_med.alert == False
    print(f"✓ Medium risk: {result_med.probability:.1%} -> {result_med.tier}")
    
    # Test High risk
    result_high = classify_risk('diabetes', 0.85, shap_vals, features)
    assert result_high.tier == 'High'
    assert result_high.color == '#FF6B6B'
    assert result_high.alert == True
    print(f"✓ High risk: {result_high.probability:.1%} -> {result_high.tier}")
    
    print()


def test_top_factors():
    """Test top factor extraction"""
    print("Testing Top Factor Extraction...")
    
    shap_vals = MockSHAPValues([0.8, -0.5, 0.3, -0.2, 0.1])
    features = ['Glucose', 'Age', 'BMI', 'BP', 'Insulin']
    
    result = classify_risk('diabetes', 0.75, shap_vals, features)
    
    print(f"Top 3 factors: {result.top_factors}")
    assert len(result.top_factors) == 3
    assert 'Glucose' in result.top_factors  # Highest absolute value
    print("✓ Top factors extracted correctly\n")


def test_recommendations():
    """Test clinical recommendations"""
    print("Testing Clinical Recommendations...")
    
    diseases = ['diabetes', 'heart', 'ckd']
    tiers = ['Low', 'Medium', 'High']
    
    for disease in diseases:
        for tier in tiers:
            rec = get_recommendation(disease, tier)
            assert len(rec) > 0
            print(f"✓ {disease.title()} - {tier}: {rec[:50]}...")
    
    print()


def test_alert_formatting():
    """Test alert message formatting"""
    print("Testing Alert Message Formatting...")
    
    shap_vals = MockSHAPValues([0.8, 0.5, 0.3])
    features = ['Glucose', 'BMI', 'Age']
    
    result = classify_risk('diabetes', 0.85, shap_vals, features)
    alert_msg = format_alert_message(result)
    
    assert '⚠️' in alert_msg
    assert 'HIGH RISK' in alert_msg
    assert 'Diabetes' in alert_msg
    print(f"✓ Alert message: {alert_msg}\n")


def test_threshold_boundaries():
    """Test threshold boundary conditions"""
    print("Testing Threshold Boundaries...")
    
    shap_vals = MockSHAPValues([0.5, 0.3, 0.2])
    features = ['F1', 'F2', 'F3']
    
    # Test exact boundaries
    result_1 = classify_risk('diabetes', 0.34, shap_vals, features)
    assert result_1.tier == 'Low'
    
    result_2 = classify_risk('diabetes', 0.35, shap_vals, features)
    assert result_2.tier == 'Medium'
    
    result_3 = classify_risk('diabetes', 0.65, shap_vals, features)
    assert result_3.tier == 'Medium'
    
    result_4 = classify_risk('diabetes', 0.66, shap_vals, features)
    assert result_4.tier == 'High'
    
    print(f"✓ Thresholds: Low < {THRESHOLDS['low_max']}, High ≥ {THRESHOLDS['high_min']}\n")


if __name__ == "__main__":
    print("="*60)
    print("Risk Engine Validation Tests")
    print("="*60 + "\n")
    
    try:
        test_risk_classification()
        test_top_factors()
        test_recommendations()
        test_alert_formatting()
        test_threshold_boundaries()
        
        print("="*60)
        print("✅ All risk engine tests passed!")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
