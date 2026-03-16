"""
Prediction Module
Loads trained models and generates disease risk predictions
"""

import joblib
import pandas as pd
from pathlib import Path
from typing import Dict, Any


class DiseasePredictor:
    """Handles model loading and prediction for disease risk assessment"""
    
    def __init__(self, models_dir: str = "models"):
        self.models_dir = Path(models_dir)
        self.models = {}
        self.disease_names = ["diabetes", "heart", "ckd"]
    
    def load_model(self, disease: str):
        """Load a trained model for specific disease"""
        model_path = self.models_dir / f"{disease}_model.pkl"
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found: {model_path}")
        
        try:
            self.models[disease] = joblib.load(model_path)
            return True
        except Exception as e:
            raise RuntimeError(f"Error loading model for {disease}: {str(e)}")
    
    def load_all_models(self):
        """Load all disease prediction models"""
        loaded = []
        for disease in self.disease_names:
            try:
                self.load_model(disease)
                loaded.append(disease)
            except FileNotFoundError:
                print(f"Warning: {disease} model not found, skipping...")
        return loaded
    
    def predict(self, disease: str, patient_data: pd.DataFrame) -> Dict[str, Any]:
        """Generate prediction for a specific disease with error handling"""
        if disease not in self.models:
            raise ValueError(f"Model for {disease} not loaded. Available models: {list(self.models.keys())}")
        
        try:
            model = self.models[disease]
            
            # Get prediction probability
            proba = model.predict_proba(patient_data)
            
            # Handle different probability array shapes
            if len(proba.shape) == 2 and proba.shape[1] == 2:
                prob = proba[0][1]  # Binary classification
            else:
                prob = proba[0][0]  # Single probability
            
            prediction = int(prob > 0.5)
            
            return {
                "disease": disease,
                "probability": float(prob),
                "prediction": prediction,
                "risk_tier": self._get_risk_tier(prob)
            }
        
        except IndexError as e:
            raise RuntimeError(f"Prediction array shape mismatch: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Prediction failed for {disease}: {str(e)}")
    
    def predict_all(self, patient_data: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
        """Generate predictions for all loaded disease models"""
        results = {}
        
        for disease in self.models.keys():
            try:
                results[disease] = self.predict(disease, patient_data)
            except Exception as e:
                results[disease] = {"error": str(e)}
        
        return results
    
    @staticmethod
    def _get_risk_tier(probability: float) -> str:
        """Classify risk probability into Low/Medium/High tiers"""
        if probability < 0.35:
            return "Low"
        elif probability <= 0.65:
            return "Medium"
        else:
            return "High"
