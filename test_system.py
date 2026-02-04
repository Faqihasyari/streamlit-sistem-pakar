"""
Test Script untuk Sistem Pakar
Menguji semua komponen sistem
"""

import sys
import os

# Tambahkan path jika perlu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from expert_system import ExpertSystem
from ml_model import MLRecommender


def test_expert_system():
    """Test Rule-Based Expert System"""
    print("\n" + "="*60)
    print("TEST 1: RULE-BASED EXPERT SYSTEM")
    print("="*60)
    
    expert = ExpertSystem()
    
    # Test case 1
    print("\n📝 Test Case 1:")
    print("   Industry: Web Development")
    print("   Career: Kerja cepat")
    print("   Priority: Banyak lowongan")
    
    candidates, scores, explanations = expert.infer(
        "Web Development", 
        "Kerja cepat", 
        "Banyak lowongan"
    )
    
    print(f"\n✅ Kandidat: {', '.join(candidates)}")
    print(f"   Jumlah: {len(candidates)}")
    
    print("\n📊 Skor:")
    for lang in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"   {lang[0]}: {lang[1]:.1f}")
    
    # Test case 2
    print("\n📝 Test Case 2:")
    print("   Industry: Data Science")
    print("   Career: Magang")
    print("   Priority: Mudah dipelajari")
    
    candidates2, scores2, explanations2 = expert.infer(
        "Data Science",
        "Magang",
        "Mudah dipelajari"
    )
    
    print(f"\n✅ Kandidat: {', '.join(candidates2)}")
    print(f"   Top recommendation: {max(scores2.items(), key=lambda x: x[1])[0]}")
    
    return True


def test_ml_model():
    """Test Machine Learning Model"""
    print("\n" + "="*60)
    print("TEST 2: MACHINE LEARNING MODEL")
    print("="*60)
    
    ml = MLRecommender()
    
    # Test training
    print("\n🔄 Testing model training...")
    result = ml.train('data/industry_data.csv')
    
    if result['success']:
        print(f"✅ Training berhasil!")
        print(f"   Accuracy: {result['accuracy']:.2%}")
        print(f"   Samples: {result['n_samples']}")
        print(f"   Classes: {result['n_classes']}")
    else:
        print(f"❌ Training gagal: {result['error']}")
        return False
    
    # Test prediction
    print("\n🔮 Testing prediction...")
    test_candidates = {"Python", "JavaScript", "PHP"}
    
    try:
        scores = ml.predict_proba(
            "Web Development",
            "Kerja cepat",
            "Banyak lowongan",
            test_candidates
        )
        
        print("✅ Prediction berhasil!")
        print("📊 ML Scores:")
        for lang, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            print(f"   {lang}: {score:.1f}%")
        
        return True
    except Exception as e:
        print(f"❌ Prediction gagal: {str(e)}")
        return False


def test_hybrid_system():
    """Test Hybrid System (Integration)"""
    print("\n" + "="*60)
    print("TEST 3: HYBRID SYSTEM (INTEGRATION)")
    print("="*60)
    
    expert = ExpertSystem()
    ml = MLRecommender()
    
    # Train ML model
    print("\n🔄 Preparing ML model...")
    ml.train('data/industry_data.csv')
    
    # Test hybrid
    print("\n🧪 Testing hybrid recommendation...")
    
    industry = "Backend Development"
    career = "Startup"
    priority = "Gaji tinggi"
    
    print(f"\n📝 Input:")
    print(f"   Industry: {industry}")
    print(f"   Career: {career}")
    print(f"   Priority: {priority}")
    
    # Rule-based
    candidates, rule_scores, explanations = expert.infer(industry, career, priority)
    
    # ML scoring
    ml_scores = ml.predict_proba(industry, career, priority, candidates)
    
    # Hybrid scoring
    final_scores = {}
    for lang in candidates:
        rule_score = rule_scores.get(lang, 0)
        ml_score = ml_scores.get(lang, 0)
        final_scores[lang] = (rule_score * 0.6) + (ml_score * 0.4)
    
    # Results
    ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n✅ Kandidat: {len(candidates)}")
    print("\n🏆 Top 3 Rekomendasi:")
    for i, (lang, score) in enumerate(ranked[:3], 1):
        rule_s = rule_scores.get(lang, 0)
        ml_s = ml_scores.get(lang, 0)
        print(f"   {i}. {lang}")
        print(f"      Rule-Based: {rule_s:.1f}")
        print(f"      ML Score: {ml_s:.1f}")
        print(f"      Final: {score:.1f}")
    
    return True


def test_language_info():
    """Test Language Information Retrieval"""
    print("\n" + "="*60)
    print("TEST 4: LANGUAGE INFORMATION")
    print("="*60)
    
    expert = ExpertSystem()
    
    test_languages = ["Python", "JavaScript", "Java"]
    industry = "Web Development"
    
    for lang in test_languages:
        print(f"\n📚 Testing {lang} info...")
        info = expert.get_language_info(lang, industry)
        
        if info:
            print(f"   ✅ Info loaded")
            print(f"   Description: {info.get('description', 'N/A')[:50]}...")
            print(f"   Pros: {len(info.get('pros', []))} items")
            print(f"   Learning time: {info.get('learning_time', 'N/A')}")
        else:
            print(f"   ⚠️ No info available")
    
    return True


def test_dataset():
    """Test Dataset Integrity"""
    print("\n" + "="*60)
    print("TEST 5: DATASET INTEGRITY")
    print("="*60)
    
    import pandas as pd
    
    try:
        df = pd.read_csv('data/industry_data.csv')
        print(f"\n✅ Dataset loaded successfully")
        print(f"   Records: {len(df)}")
        print(f"   Columns: {len(df.columns)}")
        
        print("\n📊 Dataset info:")
        print(f"   Industries: {df['industry'].nunique()}")
        print(f"   Career goals: {df['career_goal'].nunique()}")
        print(f"   Priorities: {df['priority'].nunique()}")
        print(f"   Languages: {df['language'].nunique()}")
        
        print("\n📈 Language distribution:")
        lang_counts = df['language'].value_counts()
        for lang, count in lang_counts.items():
            print(f"   {lang}: {count} records")
        
        # Check for missing values
        missing = df.isnull().sum().sum()
        if missing > 0:
            print(f"\n⚠️ Warning: {missing} missing values found")
        else:
            print(f"\n✅ No missing values")
        
        return True
        
    except Exception as e:
        print(f"❌ Dataset test failed: {str(e)}")
        return False


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("SISTEM PAKAR - COMPREHENSIVE TEST SUITE")
    print("="*60)
    
    tests = [
        ("Expert System", test_expert_system),
        ("ML Model", test_ml_model),
        ("Hybrid System", test_hybrid_system),
        ("Language Info", test_language_info),
        ("Dataset", test_dataset)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} failed with error: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n{'='*60}")
    print(f"Result: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    print(f"{'='*60}\n")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    
    if success:
        print("🎉 All tests passed! System ready for deployment.")
        sys.exit(0)
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        sys.exit(1)