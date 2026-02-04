# 🎓 Sistem Pakar Rekomendasi Bahasa Pemrograman untuk Pemula

Sistem Pakar Hybrid (Rule-Based Expert System + Machine Learning) untuk merekomendasikan bahasa pemrograman terbaik bagi pemula berdasarkan kebutuhan industri IT.

## 📋 Deskripsi

Aplikasi web berbasis Streamlit yang menggunakan pendekatan hybrid untuk memberikan rekomendasi bahasa pemrograman yang personal dan akurat:

- **Rule-Based Expert System**: Filtering kandidat bahasa menggunakan aturan IF-THEN
- **Machine Learning**: Scoring menggunakan Naive Bayes Classifier
- **Dataset**: Data kebutuhan industri IT Indonesia 2024-2025

## 🎯 Fitur Utama

- ✅ Kuesioner interaktif untuk input user
- ✅ Analisis hybrid (Rule-Based + ML)
- ✅ Ranking bahasa pemrograman dengan skor
- ✅ Penjelasan detail setiap rekomendasi
- ✅ Roadmap belajar untuk setiap bahasa
- ✅ Resources pembelajaran
- ✅ Visualisasi skor dan perbandingan
- ✅ Export hasil rekomendasi

## 🚀 Cara Menjalankan

### Lokal

1. Clone repository:
```bash
git clone <repository-url>
cd spk-bahasa-pemrograman
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Training model ML (opsional, akan otomatis jika belum ada):
```bash
python ml_model.py
```

4. Jalankan aplikasi:
```bash
streamlit run app.py
```

5. Buka browser di `http://localhost:8501`

### Deploy ke Streamlit Community Cloud

1. Push repository ke GitHub
2. Login ke [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Deploy!

## 📂 Struktur Project

```
spk-bahasa-pemrograman/
├── app.py                      # Main Streamlit application
├── expert_system.py            # Rule-Based Expert System
├── ml_model.py                 # Machine Learning module
├── requirements.txt            # Python dependencies
├── README.md                   # Dokumentasi
├── data/
│   └── industry_data.csv       # Dataset training (46 records)
├── models/
│   └── trained_model.pkl       # Saved ML model
└── utils/
    └── helpers.py              # Helper functions
```

## 🧠 Arsitektur Sistem

```
┌─────────────────────────────────────────────────────┐
│              STREAMLIT WEB APP                       │
├─────────────────────────────────────────────────────┤
│                                                       │
│  INPUT LAYER                                         │
│  └─ Kuesioner (Industry, Career Goal, Priority)     │
│                                                       │
│  INFERENCE ENGINE (HYBRID)                           │
│  ├─ Rule-Based Expert System (60%)                   │
│  │  └─ Forward Chaining IF-THEN rules               │
│  └─ Machine Learning (40%)                           │
│     └─ Naive Bayes Classifier                        │
│                                                       │
│  OUTPUT LAYER                                        │
│  └─ Ranked recommendations + explanations            │
└─────────────────────────────────────────────────────┘
```

## 📊 Dataset

Dataset berisi 46 records dengan struktur:

| Feature | Type | Values |
|---------|------|--------|
| industry | Categorical | Web Dev, Data Science, Mobile, Backend, Game |
| career_goal | Categorical | Kerja cepat, Magang, Freelance, Startup |
| priority | Categorical | Mudah dipelajari, Banyak lowongan, Gaji tinggi |
| job_demand | Ordinal | Low, Medium, High |
| learning_curve | Ordinal | Easy, Medium, Hard |
| salary_level | Ordinal | Low, Medium, High |
| community_support | Ordinal | Low, Medium, High |
| **language** (target) | Categorical | Python, JavaScript, PHP, Java, Kotlin, C#, Golang |

## 🔧 Teknologi

- **Python**: 3.8+
- **Streamlit**: Web framework
- **Scikit-learn**: Machine Learning (Naive Bayes)
- **Pandas**: Data processing
- **NumPy**: Numerical operations

## 📖 Metodologi

### 1. Rule-Based Expert System

Menggunakan 4 rule sets:

1. **Industry Rules**: Filtering bahasa berdasarkan industri
2. **Career Goal Rules**: Boost skor berdasarkan tujuan karier
3. **Priority Rules**: Boost skor berdasarkan prioritas pemula
4. **Complexity Rules**: Adjustment untuk tingkat kesulitan

### 2. Machine Learning

- **Algorithm**: Multinomial Naive Bayes
- **Training**: Supervised learning dengan dataset industri
- **Output**: Probability distribution untuk setiap bahasa
- **Integration**: Skor ML dikombinasikan dengan skor rule-based (60:40)

### 3. Hybrid Scoring

```
Final Score = (Rule-Based Score × 0.6) + (ML Score × 0.4)
```

## 🎓 Justifikasi Akademik

### Mengapa Hybrid System?

| Aspek | Rule-Based Only | ML Only | Hybrid |
|-------|----------------|---------|--------|
| Explainability | ✅ Tinggi | ❌ Rendah | ✅ Tinggi |
| Adaptability | ❌ Manual update | ✅ Auto learn | ✅ Balanced |
| Accuracy | ⚠️ Tergantung rules | ⚠️ Tergantung data | ✅ Optimal |
| Maintenance | ⚠️ Butuh expert | ⚠️ Butuh data | ✅ Fleksibel |

### Keunggulan Pendekatan

1. **Transparent**: Setiap keputusan dapat dijelaskan
2. **Data-driven**: Belajar dari tren industri real
3. **Robust**: Kombinasi logic dan statistics
4. **Practical**: Mudah di-deploy dan maintain

## 📝 Contoh Use Case

### Input:
- Industry: **Web Development**
- Career Goal: **Kerja cepat**
- Priority: **Banyak lowongan**

### Output:
1. 🥇 **JavaScript** (Skor: 92.5/100)
   - Essential untuk web frontend + backend
   - Banyak lowongan entry-level
   
2. 🥈 **Python** (Skor: 87.3/100)
   - Django/Flask untuk backend
   - Mudah dipelajari
   
3. 🥉 **PHP** (Skor: 74.8/100)
   - Laravel framework populer
   - Banyak project freelance

## 🤝 Kontribusi

Untuk tugas akademik, Anda dapat:

1. Menambahkan bahasa pemrograman baru
2. Update dataset dengan data terbaru
3. Improve rule sets
4. Tambahkan fitur visualisasi
5. Improve ML model (try Decision Tree, Random Forest)

## 📄 Lisensi

Project ini dibuat untuk tujuan akademik (tugas kuliah).

## 👨‍💻 Developer

Dikembangkan sebagai implementasi:
- Sistem Pakar (Expert Systems)
- Kecerdasan Buatan (Artificial Intelligence)
- Machine Learning

---

**Note**: Sistem ini dirancang untuk pemula dan berbasis data industri Indonesia 2024-2025. Rekomendasi dapat berubah seiring perkembangan industri IT.