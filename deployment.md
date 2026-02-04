# 🌐 Deployment Guide

Panduan lengkap untuk deploy aplikasi Sistem Pakar ke Streamlit Community Cloud.

## Prerequisites

- ✅ Repository GitHub (public atau private)
- ✅ Akun GitHub
- ✅ Akun Streamlit Cloud (gratis, login dengan GitHub)

## Persiapan Repository

### 1. Pastikan Struktur Project Benar

```
spk-bahasa-pemrograman/
├── app.py                    ✅ Main file
├── expert_system.py          ✅ Required
├── ml_model.py              ✅ Required
├── requirements.txt         ✅ PENTING!
├── data/
│   └── industry_data.csv    ✅ Dataset
├── models/
│   └── trained_model.pkl    ✅ (akan auto-generate)
└── utils/
    └── helpers.py           ✅ Required
```

### 2. Pastikan requirements.txt Lengkap

File `requirements.txt` harus berisi:

```
streamlit==1.31.0
pandas==2.1.4
numpy==1.26.3
scikit-learn==1.4.0
matplotlib==3.8.2
```

**PENTING**: Jangan gunakan versi terlalu baru yang mungkin tidak kompatibel.

### 3. Test Lokal Terlebih Dahulu

```bash
# Test aplikasi berjalan lancar
streamlit run app.py

# Test model training
python train_model.py
```

Pastikan tidak ada error!

## Deploy ke Streamlit Community Cloud

### Langkah 1: Push ke GitHub

```bash
# Inisialisasi Git (jika belum)
cd spk-bahasa-pemrograman
git init

# Add remote repository
git remote add origin https://github.com/USERNAME/REPO-NAME.git

# Add semua file
git add .

# Commit
git commit -m "Initial commit - SPK Bahasa Pemrograman"

# Push ke GitHub
git push -u origin main
```

**Note**: Ganti `USERNAME` dan `REPO-NAME` dengan milik Anda.

### Langkah 2: Buka Streamlit Cloud

1. Buka https://share.streamlit.io
2. Klik **"Sign in with GitHub"**
3. Authorize Streamlit untuk akses GitHub

### Langkah 3: Deploy App

1. Klik tombol **"New app"** atau **"Create app"**

2. **Fill deployment form**:
   - **Repository**: Pilih repo `spk-bahasa-pemrograman`
   - **Branch**: `main` (atau `master`)
   - **Main file path**: `app.py`
   - **App URL** (optional): Bisa customize URL

3. **Advanced settings** (optional):
   - Python version: 3.9 atau 3.10
   - Secrets: Tidak perlu untuk app ini

4. Klik **"Deploy!"**

### Langkah 4: Tunggu Deployment

```
⏳ Building... (1-2 menit)
   ├─ Installing dependencies
   ├─ Setting up environment
   └─ Starting app

✅ Your app is live! (2-5 menit total)
```

### Langkah 5: Test App

1. Klik URL yang diberikan (misal: `https://your-app.streamlit.app`)
2. Test semua fitur:
   - ✅ Kuesioner berfungsi
   - ✅ Rekomendasi muncul
   - ✅ Chart ditampilkan
   - ✅ Export download bekerja

## Troubleshooting Deployment

### Error: Requirements installation failed

**Solusi 1**: Update requirements.txt dengan versi kompatibel
```
streamlit>=1.28.0,<1.35.0
pandas>=2.0.0,<3.0.0
scikit-learn>=1.3.0,<1.5.0
```

**Solusi 2**: Pin versi spesifik yang Anda gunakan lokal
```bash
pip freeze | grep streamlit >> requirements.txt
```

### Error: Module not found

**Penyebab**: File tidak terupload atau struktur salah

**Solusi**:
1. Pastikan semua file ter-commit
2. Cek struktur folder di GitHub
3. Pastikan path import benar

### Error: Model training failed

**Penyebab**: Dataset tidak ditemukan

**Solusi**:
1. Pastikan `data/industry_data.csv` ada di GitHub
2. Cek path di `ml_model.py`: 
   ```python
   ml.train('data/industry_data.csv')
   ```

### App running but slow

**Penyebab**: Free tier memiliki resource terbatas

**Solusi**:
1. Optimize dengan caching:
   ```python
   @st.cache_resource
   def load_model():
       ...
   ```
2. Pre-train model (include .pkl di repo)
3. Upgrade ke paid tier (jika perlu)

### App crashes randomly

**Penyebab**: Memory limit exceeded

**Solusi**:
1. Kurangi ukuran dataset
2. Optimize code
3. Clear cache secara berkala

## Update Aplikasi

### Update Kode

```bash
# Edit file lokal
nano app.py

# Test lokal
streamlit run app.py

# Commit dan push
git add .
git commit -m "Update: fitur baru XYZ"
git push
```

**Streamlit Cloud akan auto-deploy** dalam 1-2 menit!

### Update Dataset

```bash
# Edit dataset
nano data/industry_data.csv

# Re-train model
python train_model.py

# Push ke GitHub
git add data/industry_data.csv models/trained_model.pkl
git commit -m "Update dataset"
git push
```

### Rollback ke Versi Sebelumnya

```bash
# Lihat commit history
git log

# Rollback ke commit tertentu
git revert <commit-hash>
git push
```

## Monitoring & Maintenance

### Melihat Logs

1. Buka app di Streamlit Cloud dashboard
2. Klik **"Manage app"**
3. Lihat tab **"Logs"** untuk error messages

### Analytics

Streamlit Cloud (free tier) tidak punya analytics built-in, tapi Anda bisa:

1. Tambahkan Google Analytics
2. Gunakan Streamlit secrets untuk tracking
3. Log user interactions ke file

### Restart App

Jika app bermasalah:
1. Buka dashboard Streamlit Cloud
2. Klik **"Reboot app"**
3. Atau push dummy commit untuk trigger rebuild

## Best Practices

### ✅ DO's

- ✅ Test lokal sebelum deploy
- ✅ Gunakan `.gitignore` untuk exclude unnecessary files
- ✅ Pin dependency versions di requirements.txt
- ✅ Include trained model di repo (jika <100MB)
- ✅ Dokumentasi README.md yang jelas
- ✅ Gunakan caching (@st.cache_resource)

### ❌ DON'Ts

- ❌ Jangan commit API keys atau secrets
- ❌ Jangan include virtual environment (venv/)
- ❌ Jangan push file terlalu besar (>100MB)
- ❌ Jangan hardcode paths (gunakan relative paths)
- ❌ Jangan skip testing lokal

## Alternative Deployment Platforms

Jika Streamlit Cloud tidak cocok:

### 1. Heroku

```bash
# Tambahkan Procfile
echo "web: streamlit run app.py" > Procfile

# Deploy
heroku create
git push heroku main
```

### 2. Railway

- Upload repo ke Railway
- Set build command: `pip install -r requirements.txt`
- Set start command: `streamlit run app.py --server.port $PORT`

### 3. Google Cloud Run

```bash
# Build container
gcloud builds submit --tag gcr.io/PROJECT-ID/spk-app

# Deploy
gcloud run deploy --image gcr.io/PROJECT-ID/spk-app
```

### 4. Render

- Connect GitHub repo
- Environment: Python
- Build command: `pip install -r requirements.txt`
- Start command: `streamlit run app.py`

## Sharing Your App

### Share Link

```
Public URL: https://your-app.streamlit.app
```

Share link ini untuk:
- Presentasi tugas kuliah
- Demo ke dosen
- Portfolio
- CV/Resume

### Embed di Website

```html
<iframe 
  src="https://your-app.streamlit.app/?embedded=true" 
  height="800" 
  width="100%"
></iframe>
```

### QR Code

Generate QR code untuk link app Anda:
- https://qr-code-generator.com/
- Cetak untuk presentasi

## Support & Resources

- 📖 [Streamlit Docs](https://docs.streamlit.io/)
- 💬 [Streamlit Forum](https://discuss.streamlit.io/)
- 🐙 [GitHub Issues](https://github.com/streamlit/streamlit/issues)
- 📺 [YouTube Tutorials](https://www.youtube.com/c/Streamlit)

---

**Good luck with your deployment!** 🚀

Jangan lupa star repo ini di GitHub jika bermanfaat! ⭐