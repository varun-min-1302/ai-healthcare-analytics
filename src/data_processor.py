"""
Data Processing Module
Handles data loading, validation, preprocessing, and feature engineering
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from typing import Tuple, Dict, Any


# Feature configurations for each disease module
FEATURE_CONFIGS = {
    'diabetes': {
        'features': ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'],
        'zero_impute_cols': ['Glucose', 'BloodPressure', 'BMI'],
        'target': 'Outcome'
    },
    'heart': {
        'features': ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'],
        'zero_impute_cols': [],
        'target': 'target'
    },
    'ckd': {
        'features': ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 
                    'pot', 'hemo', 'pcv', 'wbcc', 'rbcc', 'htn', 'dm', 'cad', 
                    'appet', 'pe', 'ane'],
        'zero_impute_cols': [],
        'target': 'classification'
    }
}


class DataProcessor:
    """Handles all data preprocessing operations for patient health data"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
    
    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load patient data from CSV file"""
        try:
            df = pd.read_csv(filepath)
            return df
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def validate_data(self, df: pd.DataFrame, required_columns: list) -> Tuple[bool, str]:
        """Validate that dataframe contains required columns"""
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            return False, f"Missing required columns: {missing_cols}"
        return True, "Validation passed"
    
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Impute missing values: median for numeric, mode for categorical"""
        df_clean = df.copy()
        
        # Drop columns with >40% missing values
        threshold = 0.4
        missing_pct = df_clean.isnull().sum() / len(df_clean)
        cols_to_drop = missing_pct[missing_pct > threshold].index
        df_clean = df_clean.drop(columns=cols_to_drop)
        
        # Impute remaining nulls
        for col in df_clean.columns:
            if df_clean[col].isnull().any():
                if df_clean[col].dtype in ['float64', 'int64']:
                    df_clean[col].fillna(df_clean[col].median(), inplace=True)
                else:
                    df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
        
        return df_clean
    
    def encode_categorical(self, df: pd.DataFrame, categorical_cols: list) -> pd.DataFrame:
        """Encode categorical variables"""
        df_encoded = df.copy()
        
        for col in categorical_cols:
            if col in df_encoded.columns:
                le = LabelEncoder()
                df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
                self.label_encoders[col] = le
        
        return df_encoded
    
    def preprocess_pipeline(self, df: pd.DataFrame, target_col: str = None) -> pd.DataFrame:
        """Complete preprocessing pipeline"""
        # Handle missing values
        df_processed = self.handle_missing_values(df)
        
        # Identify categorical columns
        categorical_cols = df_processed.select_dtypes(include=['object']).columns.tolist()
        if target_col and target_col in categorical_cols:
            categorical_cols.remove(target_col)
        
        # Encode categorical variables
        if categorical_cols:
            df_processed = self.encode_categorical(df_processed, categorical_cols)
        
        return df_processed
    
    def validate_and_preprocess(self, df: pd.DataFrame, disease: str) -> pd.DataFrame:
        """Disease-specific validation and preprocessing"""
        if disease not in FEATURE_CONFIGS:
            raise ValueError(f"Unknown disease: {disease}. Must be one of {list(FEATURE_CONFIGS.keys())}")
        
        config = FEATURE_CONFIGS[disease]
        
        # Check for empty dataframe
        if df.empty:
            raise ValueError("DataFrame is empty. Please provide valid patient data.")
        
        # Check for missing columns
        missing = [f for f in config['features'] if f not in df.columns]
        if missing:
            raise ValueError(f'Missing required columns for {disease}: {missing}')
        
        # Select only required features
        df_clean = df[config['features']].copy()
        
        # Replace zeros with NaN for biological impossibilities
        for col in config['zero_impute_cols']:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].replace(0, np.nan)
        
        # Impute missing values with median
        df_clean.fillna(df_clean.median(numeric_only=True), inplace=True)
        
        return df_clean
    
    def validate_csv(self, df: pd.DataFrame, disease: str) -> Tuple[bool, str]:
        """Validate CSV format and columns"""
        if df.empty:
            return False, "CSV file is empty. Please provide valid patient data."
        
        if disease not in FEATURE_CONFIGS:
            return False, f"Unknown disease: {disease}"
        
        config = FEATURE_CONFIGS[disease]
        required = set(config['features'])
        provided = set(df.columns)
        
        missing = required - provided
        extra = provided - required
        
        if missing:
            return False, f"Missing required columns: {', '.join(missing)}"
        
        if extra:
            # Extra columns are OK, just warn
            return True, f"Note: Extra columns will be ignored: {', '.join(extra)}"
        
        return True, "Validation passed"
