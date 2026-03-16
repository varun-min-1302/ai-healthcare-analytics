"""
Test script for data_processor module
Validates preprocessing functionality with sample data
"""

import sys
sys.path.append('.')

from src.data_processor import DataProcessor, FEATURE_CONFIGS
import pandas as pd

def test_diabetes_preprocessing():
    """Test diabetes data preprocessing"""
    print("Testing Diabetes Preprocessing...")
    
    processor = DataProcessor()
    df = pd.read_csv('data/sample/diabetes_test.csv')
    
    print(f"Original shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    # Validate and preprocess
    df_clean = processor.validate_and_preprocess(df, 'diabetes')
    
    print(f"Processed shape: {df_clean.shape}")
    print(f"Missing values: {df_clean.isnull().sum().sum()}")
    print("✓ Diabetes preprocessing successful\n")
    
    return df_clean

def test_heart_preprocessing():
    """Test heart disease data preprocessing"""
    print("Testing Heart Disease Preprocessing...")
    
    processor = DataProcessor()
    df = pd.read_csv('data/sample/heart_test.csv')
    
    print(f"Original shape: {df.shape}")
    df_clean = processor.validate_and_preprocess(df, 'heart')
    
    print(f"Processed shape: {df_clean.shape}")
    print(f"Missing values: {df_clean.isnull().sum().sum()}")
    print("✓ Heart preprocessing successful\n")
    
    return df_clean

def test_ckd_preprocessing():
    """Test CKD data preprocessing"""
    print("Testing CKD Preprocessing...")
    
    processor = DataProcessor()
    df = pd.read_csv('data/sample/ckd_test.csv')
    
    print(f"Original shape: {df.shape}")
    df_clean = processor.validate_and_preprocess(df, 'ckd')
    
    print(f"Processed shape: {df_clean.shape}")
    print(f"Missing values: {df_clean.isnull().sum().sum()}")
    print("✓ CKD preprocessing successful\n")
    
    return df_clean

if __name__ == "__main__":
    print("="*60)
    print("Data Processor Validation Tests")
    print("="*60 + "\n")
    
    try:
        test_diabetes_preprocessing()
        test_heart_preprocessing()
        test_ckd_preprocessing()
        
        print("="*60)
        print("✅ All preprocessing tests passed!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
