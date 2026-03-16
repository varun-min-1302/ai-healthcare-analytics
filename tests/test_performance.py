"""
Performance Testing Suite
Validates performance benchmarks for deployment
"""

import sys
sys.path.append('.')

import pandas as pd
import time
from src.data_processor import DataProcessor


# Performance targets
TARGETS = {
    'single_patient_preprocessing': 0.1,  # 100ms
    'batch_50_preprocessing': 2.0,        # 2 seconds
    'csv_validation': 0.05,               # 50ms
}


def test_single_patient_performance():
    """Test single patient processing time"""
    print("\n" + "="*60)
    print("Performance Test: Single Patient")
    print("="*60)
    
    processor = DataProcessor()
    df = pd.read_csv('data/sample/diabetes_test.csv')
    patient = df.iloc[[0]]
    
    # Warm-up
    processor.validate_and_preprocess(patient, 'diabetes')
    
    # Timed run
    times = []
    for _ in range(10):
        start = time.time()
        processor.validate_and_preprocess(patient, 'diabetes')
        elapsed = time.time() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    target = TARGETS['single_patient_preprocessing']
    
    print(f"\nAverage time: {avg_time*1000:.2f}ms")
    print(f"Target: < {target*1000:.0f}ms")
    
    if avg_time < target:
        print("✅ PASS")
        return True
    else:
        print(f"❌ FAIL - {(avg_time/target - 1)*100:.1f}% over target")
        return False


def test_batch_performance():
    """Test batch processing performance"""
    print("\n" + "="*60)
    print("Performance Test: Batch Processing")
    print("="*60)
    
    processor = DataProcessor()
    
    # Create 50-row batch by repeating test data
    df = pd.read_csv('data/sample/diabetes_test.csv')
    batch_df = pd.concat([df] * 10, ignore_index=True)  # 5 * 10 = 50 rows
    
    print(f"Batch size: {len(batch_df)} patients")
    
    # Timed run
    start = time.time()
    processor.validate_and_preprocess(batch_df, 'diabetes')
    elapsed = time.time() - start
    
    target = TARGETS['batch_50_preprocessing']
    
    print(f"\nProcessing time: {elapsed:.3f}s")
    print(f"Target: < {target:.1f}s")
    print(f"Per patient: {elapsed/len(batch_df)*1000:.2f}ms")
    
    if elapsed < target:
        print("✅ PASS")
        return True
    else:
        print(f"❌ FAIL - {(elapsed/target - 1)*100:.1f}% over target")
        return False


def test_csv_validation_performance():
    """Test CSV validation speed"""
    print("\n" + "="*60)
    print("Performance Test: CSV Validation")
    print("="*60)
    
    processor = DataProcessor()
    df = pd.read_csv('data/sample/diabetes_test.csv')
    
    # Timed run
    times = []
    for _ in range(100):
        start = time.time()
        processor.validate_csv(df, 'diabetes')
        elapsed = time.time() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    target = TARGETS['csv_validation']
    
    print(f"\nAverage time: {avg_time*1000:.2f}ms")
    print(f"Target: < {target*1000:.0f}ms")
    
    if avg_time < target:
        print("✅ PASS")
        return True
    else:
        print(f"❌ FAIL - {(avg_time/target - 1)*100:.1f}% over target")
        return False


def run_performance_tests():
    """Run all performance tests"""
    print("\n" + "="*60)
    print("PERFORMANCE BENCHMARK SUITE")
    print("="*60)
    
    tests = [
        test_single_patient_performance,
        test_batch_performance,
        test_csv_validation_performance
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
            results.append(False)
    
    # Summary
    print("\n" + "="*60)
    print("PERFORMANCE SUMMARY")
    print("="*60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total}")
    
    if all(results):
        print("\n✅ All performance targets met!")
        print("Ready for Streamlit Cloud deployment")
    else:
        print(f"\n⚠️ {total - passed} benchmark(s) failed")
        print("Consider optimization before deployment")
    
    return all(results)


if __name__ == "__main__":
    success = run_performance_tests()
    sys.exit(0 if success else 1)
