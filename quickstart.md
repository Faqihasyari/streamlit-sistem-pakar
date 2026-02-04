# 🚀 Quick Start Guide

Panduan cepat untuk menjalankan aplikasi Sistem Pakar Rekomendasi Bahasa Pemrograman.

## Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Git (untuk cloning repository)

## Langkah 1: Setup Environment

### Clone atau Download Project

```bash
# Clone dari GitHub (jika sudah di push)
git clone <repository-url>
cd spk-bahasa-pemrograman

# ATAU download dan extract ZIP
```

### Install Dependencies

```bash
# Install semua package yang diperlukan
pip install -r requirements.txt
```

**Packages yang akan diinstall:**
- streamlit (web framework)
- pandas (data processing)
- numpy (numerical computing)
- scikit-learn (machine learning)
- matplotlib (visualization)

## Langkah 2: Training Model (Opsional)

Model ML akan otomatis ditraining saat pertama kali aplikasi dijalankan. Namun Anda bisa training manual:

```bash
python train_model.py
```

**Output yang diharapkan:**
```
✅ Model training completed!
   Accuracy: 73.91%
   Samples: 46
   Classes: 7
```

## Langkah 3: Jalankan Aplikasi

```bash
streamlit run app.py
```

**Output yang diharapkan:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

## Langkah 4: Gunakan Aplikasi

1. Buka browser di `http://localhost:8501`
2. Klik tab **"Cari Rekomendasi"**
3. Isi kuesioner di sidebar:
   - Pilih bidang industri
   - Pilih tujuan karier
   - Pilih prioritas
4. Klik **"Cari Rekomendasi"**
5. Lihat hasil rekomendasi!

## Troubleshooting

### Error: Module not found

```bash
# Pastikan semua dependencies terinstall
pip install -r requirements.txt --upgrade
```

### Error: File not found

```bash
# Pastikan Anda berada di root directory project
cd spk-bahasa-pemrograman
ls -la  # Harus melihat app.py, data/, dll
```

### Error: Port already in use

```bash
# Gunakan port berbeda
streamlit run app.py --server.port 8502
```

### Model tidak terlatih

```bash
# Training manual
python train_model.py

# Atau hapus model lama dan restart app
rm models/trained_model.pkl
streamlit run app.py
```

## Deploy ke Cloud

### Streamlit Community Cloud (Gratis)

1. **Push ke GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy di Streamlit Cloud**
   - Buka https://share.streamlit.io
   - Login dengan GitHub
   - Klik "New app"
   - Pilih repository Anda
   - Set Main file: `app.py`
   - Klik "Deploy"

3. **Tunggu deployment selesai** (~2-5 menit)

4. **Akses aplikasi** di URL yang diberikan

### Alternatif: Heroku, Railway, Render

Lihat dokumentasi masing-masing platform untuk deployment Streamlit app.

## Tips Penggunaan

### Untuk Presentasi Tugas

1. **Demo Langsung**: Jalankan lokal untuk presentasi
2. **Share Link**: Deploy ke cloud dan share URL
3. **Screenshot**: Ambil screenshot hasil rekomendasi
4. **Video**: Record screen saat menggunakan aplikasi

### Untuk Development

1. **Edit Code**: Streamlit auto-reload saat file berubah
2. **Test Dataset**: Edit `data/industry_data.csv` untuk experiment
3. **Adjust Rules**: Modifikasi `expert_system.py` untuk tuning rules
4. **Improve UI**: Edit `app.py` untuk customize tampilan

### Untuk Dokumentasi Akademik

1. **Flowchart**: Gunakan `README.md` untuk arsitektur
2. **Code Explanation**: Setiap file punya docstring lengkap
3. **Methodology**: Lihat bagian "Metodologi" di README
4. **Results**: Export hasil ke TXT untuk lampiran

## Next Steps

- 📖 Baca `README.md` untuk dokumentasi lengkap
- 🔧 Explore kode di `expert_system.py` dan `ml_model.py`
- 📊 Analisis dataset di `data/industry_data.csv`
- 🎨 Customize UI di `app.py`

## Support

Jika ada pertanyaan atau issue:

1. Cek dokumentasi di `README.md`
2. Review kode comments di setiap file
3. Test dengan input berbeda
4. Check console untuk error messages

---

**Happy Coding!** 🚀