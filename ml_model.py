"""
Machine Learning Recommender
Menggunakan Naive Bayes untuk scoring bahasa pemrograman
berdasarkan data industri
"""

import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import pickle
import os


class MLRecommender:
    def __init__(self):
        self.model = MultinomialNB(alpha=1.0)
        self.encoders = {}
        self.feature_columns = [
            'industry', 'career_goal', 'priority', 
            'job_demand', 'learning_curve', 
            'salary_level', 'community_support'
        ]
        self.classes_ = None
        self.is_trained = False
        
    def train(self, dataset_path='data/industry_data.csv'):
        """
        Melatih model dengan dataset industri
        
        Args:
            dataset_path: Path ke file CSV dataset
            
        Returns:
            Dictionary dengan informasi training
        """
        try:
            # Load dataset
            df = pd.read_csv(dataset_path)
            print(f"Dataset loaded: {len(df)} records")
            
            # Encode categorical features
            X_encoded = []
            for col in self.feature_columns:
                if col not in df.columns:
                    raise ValueError(f"Column {col} not found in dataset")
                
                self.encoders[col] = LabelEncoder()
                encoded = self.encoders[col].fit_transform(df[col])
                X_encoded.append(encoded)
            
            # Prepare training data
            X = np.array(X_encoded).T
            y = df['language'].values
            
            # Train model
            self.model.fit(X, y)
            self.classes_ = self.model.classes_
            self.is_trained = True
            
            # Calculate training accuracy
            train_accuracy = self.model.score(X, y)
            
            print(f"Model trained successfully!")
            print(f"Training accuracy: {train_accuracy:.2%}")
            print(f"Classes: {', '.join(self.classes_)}")
            
            return {
                'success': True,
                'accuracy': train_accuracy,
                'n_samples': len(df),
                'n_classes': len(self.classes_)
            }
            
        except Exception as e:
            print(f"Error during training: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def predict_proba(self, industry, career_goal, priority, candidate_languages):
        """
        Memprediksi probabilitas untuk kandidat bahasa
        
        Args:
            industry: Bidang industri
            career_goal: Tujuan karier
            priority: Prioritas pemula
            candidate_languages: Set bahasa kandidat dari expert system
            
        Returns:
            Dictionary {language: probability_score}
        """
        if not self.is_trained:
            raise ValueError("Model belum dilatih! Jalankan train() terlebih dahulu")
        
        try:
            # Encode input features
            input_encoded = []
            
            # Encode kategori input
            input_encoded.append(
                self.encoders['industry'].transform([industry])[0]
            )
            input_encoded.append(
                self.encoders['career_goal'].transform([career_goal])[0]
            )
            input_encoded.append(
                self.encoders['priority'].transform([priority])[0]
            )
            
            # Tambahkan fitur default (rata-rata dari training data)
            # job_demand, learning_curve, salary_level, community_support
            # Kita gunakan nilai "Medium"/"Medium"/"Medium"/"High" sebagai default
            default_features = ['High', 'Easy', 'Medium', 'High']
            for i, col in enumerate(['job_demand', 'learning_curve', 'salary_level', 'community_support']):
                try:
                    encoded_val = self.encoders[col].transform([default_features[i]])[0]
                    input_encoded.append(encoded_val)
                except:
                    # Jika nilai tidak ditemukan, gunakan nilai tengah
                    input_encoded.append(1)
            
            # Predict probabilitas untuk semua kelas
            X_input = np.array(input_encoded).reshape(1, -1)
            probas = self.model.predict_proba(X_input)[0]
            
            # Filter hanya kandidat dari rule-based system
            results = {}
            for lang in candidate_languages:
                if lang in self.classes_:
                    idx = list(self.classes_).index(lang)
                    # Convert to percentage (0-100)
                    results[lang] = probas[idx] * 100
                else:
                    # Jika bahasa tidak ada di training data, beri skor default rendah
                    results[lang] = 10.0
            
            return results
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            # Return default scores jika error
            return {lang: 50.0 for lang in candidate_languages}
    
    def get_feature_importance(self):
        """
        Mendapatkan informasi tentang fitur yang paling berpengaruh
        (Simplified version karena Naive Bayes tidak punya feature importance langsung)
        
        Returns:
            Dictionary dengan informasi model
        """
        if not self.is_trained:
            return None
        
        return {
            'model_type': 'Multinomial Naive Bayes',
            'n_features': len(self.feature_columns),
            'features': self.feature_columns,
            'n_classes': len(self.classes_),
            'classes': list(self.classes_)
        }
    
    def save_model(self, filepath='models/trained_model.pkl'):
        """
        Menyimpan model yang sudah dilatih
        
        Args:
            filepath: Path untuk menyimpan model
        """
        if not self.is_trained:
            raise ValueError("Model belum dilatih!")
        
        # Buat direktori jika belum ada
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Simpan model dan encoders
        model_data = {
            'model': self.model,
            'encoders': self.encoders,
            'feature_columns': self.feature_columns,
            'classes': self.classes_
        }
        
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath='models/trained_model.pkl'):
        """
        Memuat model yang sudah disimpan
        
        Args:
            filepath: Path file model
        """
        try:
            with open(filepath, 'rb') as f:
                model_data = pickle.load(f)
            
            self.model = model_data['model']
            self.encoders = model_data['encoders']
            self.feature_columns = model_data['feature_columns']
            self.classes_ = model_data['classes']
            self.is_trained = True
            
            print(f"Model loaded from {filepath}")
            return True
            
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return False
    
    def explain_prediction(self, language, probability):
        """
        Menjelaskan prediksi ML
        
        Args:
            language: Bahasa yang diprediksi
            probability: Probabilitas prediksi
            
        Returns:
            String penjelasan
        """
        confidence = "Tinggi" if probability > 70 else "Sedang" if probability > 40 else "Rendah"
        
        explanation = f"**Analisis Machine Learning:**\n\n"
        explanation += f"Probabilitas: {probability:.1f}%\n"
        explanation += f"Confidence Level: {confidence}\n\n"
        
        if probability > 70:
            explanation += "Model sangat yakin bahwa bahasa ini cocok berdasarkan data industri historis."
        elif probability > 40:
            explanation += "Model menunjukkan bahasa ini cukup relevan dengan kebutuhan Anda."
        else:
            explanation += "Model menunjukkan relevansi moderat. Pertimbangkan opsi lain juga."
        
        return explanation


def train_and_save_model():
    """
    Utility function untuk training model
    Bisa dijalankan terpisah untuk prepare model
    """
    print("="*50)
    print("Training Machine Learning Model")
    print("="*50)
    
    ml = MLRecommender()
    result = ml.train('data/industry_data.csv')
    
    if result['success']:
        ml.save_model('models/trained_model.pkl')
        print("\n✅ Model training completed!")
        print(f"   Accuracy: {result['accuracy']:.2%}")
        print(f"   Samples: {result['n_samples']}")
        print(f"   Classes: {result['n_classes']}")
    else:
        print("\n❌ Model training failed!")
        print(f"   Error: {result['error']}")
    
    return ml


if __name__ == "__main__":
    # Test training
    train_and_save_model()