"""
Script untuk training Machine Learning model
Jalankan script ini sebelum menjalankan aplikasi Streamlit
"""

from ml_model import train_and_save_model
import os


def main():
    print("\n" + "="*60)
    print("TRAINING MACHINE LEARNING MODEL")
    print("Sistem Pakar Rekomendasi Bahasa Pemrograman")
    print("="*60 + "\n")
    
    # Cek apakah dataset ada
    dataset_path = 'data/industry_data.csv'
    if not os.path.exists(dataset_path):
        print(f"❌ Error: Dataset tidak ditemukan di {dataset_path}")
        print("   Pastikan file industry_data.csv ada di folder data/")
        return
    
    # Train model
    print("📊 Memulai training model...")
    print(f"📁 Dataset: {dataset_path}\n")
    
    model = train_and_save_model()
    
    print("\n" + "="*60)
    print("TRAINING SELESAI!")
    print("="*60)
    print("\n✅ Model berhasil disimpan di models/trained_model.pkl")
    print("🚀 Anda sekarang dapat menjalankan aplikasi dengan:")
    print("   streamlit run app.py\n")


if __name__ == "__main__":
    main()