"""
Aplikasi Streamlit - Sistem Pakar Rekomendasi Bahasa Pemrograman
Sistem Hybrid: Rule-Based Expert System + Machine Learning
"""

import streamlit as st
import pandas as pd
import os
from expert_system import ExpertSystem
from ml_model import MLRecommender
from utils.helpers import (
    display_language_card, 
    display_comparison_table,
    display_learning_roadmap,
    display_resources,
    export_to_text,
    create_score_dataframe
)

# Page configuration
st.set_page_config(
    page_title="Rekomendasi Bahasa Pemrograman",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .stProgress > div > div > div > div {
        background-color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_expert_system():
    """Load expert system (cached)"""
    return ExpertSystem()


@st.cache_resource
def load_ml_model():
    """Load ML model (cached)"""
    ml = MLRecommender()
    
    # Cek apakah model sudah ada
    model_path = 'models/trained_model.pkl'
    if os.path.exists(model_path):
        ml.load_model(model_path)
    else:
        # Train model jika belum ada
        st.info("Training model untuk pertama kali...")
        result = ml.train('data/industry_data.csv')
        if result['success']:
            ml.save_model(model_path)
            st.success("Model berhasil dilatih!")
        else:
            st.error("Gagal melatih model!")
    
    return ml


def main():
    # Header
    st.markdown('<p class="main-header">🎓 Sistem Pakar Rekomendasi Bahasa Pemrograman</p>', 
                unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Sistem Hybrid untuk Pemula Berdasarkan Kebutuhan Industri IT</p>', 
                unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Cari Rekomendasi", "ℹ️ Tentang Sistem"])
    
    with tab1:
        show_home_page()
    
    with tab2:
        show_recommendation_page()
    
    with tab3:
        show_about_page()


def show_home_page():
    """Halaman beranda"""
    st.markdown("### Selamat Datang! 👋")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h4>🎯 Apa itu sistem ini?</h4>
        <p>Sistem pakar hybrid yang menggabungkan <b>Rule-Based Expert System</b> 
        dan <b>Machine Learning</b> untuk merekomendasikan bahasa pemrograman 
        terbaik bagi pemula berdasarkan kebutuhan industri IT.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
        <h4>🎓 Untuk siapa?</h4>
        <p>Dirancang khusus untuk <b>pemula</b> yang ingin memulai karier 
        di bidang IT dan bingung memilih bahasa pemrograman pertama.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h4>🔧 Teknologi yang digunakan</h4>
        <ul>
        <li><b>Rule-Based System:</b> Aturan IF-THEN untuk filtering</li>
        <li><b>Machine Learning:</b> Naive Bayes untuk scoring</li>
        <li><b>Dataset:</b> Data kebutuhan industri IT 2024-2025</li>
        <li><b>Platform:</b> Streamlit Python</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
        <h4>📊 Bahasa yang dipertimbangkan</h4>
        <p>Python 🐍, JavaScript 🟨, PHP 🐘, Java ☕, Kotlin 🅺, C# #️⃣, Golang 🔷</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick start button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🚀 Siap untuk mencari rekomendasi?")
        st.markdown("Klik tab **Cari Rekomendasi** di atas untuk memulai!")


def show_recommendation_page():
    """Halaman utama untuk rekomendasi"""
    
    # Sidebar - Input Form
    st.sidebar.header("📋 Kuesioner")
    st.sidebar.markdown("Jawab pertanyaan di bawah untuk mendapatkan rekomendasi:")
    
    with st.sidebar.form("input_form"):
        industry = st.selectbox(
            "1️⃣ Bidang Industri yang Diminati:",
            ["Web Development", "Data Science", "Mobile Development", 
             "Backend Development", "Game Development"],
            help="Pilih bidang IT yang paling Anda minati"
        )
        
        career_goal = st.selectbox(
            "2️⃣ Tujuan Karier:",
            ["Kerja cepat", "Magang", "Freelance", "Startup"],
            help="Apa tujuan karier Anda dalam waktu dekat?"
        )
        
        priority = st.selectbox(
            "3️⃣ Prioritas sebagai Pemula:",
            ["Mudah dipelajari", "Banyak lowongan", "Gaji tinggi"],
            help="Apa yang paling penting bagi Anda?"
        )
        
        submit_button = st.form_submit_button("🔍 Cari Rekomendasi", use_container_width=True)
    
    # Main content area
    if submit_button:
        process_recommendation(industry, career_goal, priority)
    else:
        # Default state - show instructions
        st.info("👈 Silakan isi kuesioner di sidebar untuk mendapatkan rekomendasi bahasa pemrograman!")
        
        # Show sample visualization
        st.markdown("### 📊 Preview: Contoh Hasil Rekomendasi")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Top 1", "Python 🐍", "95/100")
        with col2:
            st.metric("Top 2", "JavaScript 🟨", "87/100")
        with col3:
            st.metric("Top 3", "PHP 🐘", "72/100")
        
        # Sample chart
        sample_data = pd.DataFrame({
            'Bahasa': ['Python', 'JavaScript', 'PHP', 'Java'],
            'Skor': [95, 87, 72, 65]
        })
        st.bar_chart(sample_data.set_index('Bahasa'))


def process_recommendation(industry, career_goal, priority):
    """
    Memproses rekomendasi menggunakan hybrid system
    """
    st.markdown("## 🎯 Hasil Rekomendasi")
    
    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Load systems
    status_text.text("⚙️ Memuat sistem pakar...")
    progress_bar.progress(20)
    expert = load_expert_system()
    
    status_text.text("🤖 Memuat model machine learning...")
    progress_bar.progress(40)
    ml_model = load_ml_model()
    
    # TAHAP 1: Rule-Based Expert System
    status_text.text("📊 Tahap 1: Menjalankan sistem pakar (Rule-Based)...")
    progress_bar.progress(60)
    
    candidates, rule_scores, explanations = expert.infer(industry, career_goal, priority)
    
    # TAHAP 2: Machine Learning Scoring
    status_text.text("🤖 Tahap 2: Menghitung skor ML (Naive Bayes)...")
    progress_bar.progress(80)
    
    ml_scores = ml_model.predict_proba(industry, career_goal, priority, candidates)
    
    # Gabungkan skor: 60% Rule-Based + 40% ML
    final_scores = {}
    for lang in candidates:
        rule_score = rule_scores.get(lang, 0)
        ml_score = ml_scores.get(lang, 0)
        final_scores[lang] = (rule_score * 0.6) + (ml_score * 0.4)
    
    # Ranking
    ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
    
    progress_bar.progress(100)
    status_text.text("✅ Rekomendasi siap!")
    
    # Clear progress
    import time
    time.sleep(0.5)
    progress_bar.empty()
    status_text.empty()
    
    # Display results
    display_results(ranked, industry, career_goal, priority, expert, ml_scores, rule_scores, explanations)


def display_results(ranked, industry, career_goal, priority, expert, ml_scores, rule_scores, explanations):
    """Menampilkan hasil rekomendasi"""
    
    # Summary box
    st.markdown(f"""
    <div class="info-box">
    <h4>📝 Ringkasan Input Anda:</h4>
    <ul>
    <li><b>Bidang Industri:</b> {industry}</li>
    <li><b>Tujuan Karier:</b> {career_goal}</li>
    <li><b>Prioritas:</b> {priority}</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### 🏆 Ditemukan {len(ranked)} kandidat bahasa pemrograman")
    
    # Top 3 recommendations in columns
    st.markdown("---")
    st.markdown("### 🥇 Top 3 Rekomendasi")
    
    cols = st.columns(3)
    for i, (lang, score) in enumerate(ranked[:3]):
        with cols[i]:
            info = expert.get_language_info(lang, industry)
            display_language_card(lang, score, i+1, info, industry)
    
    # Detailed view for top recommendation
    st.markdown("---")
    st.markdown("### 📖 Detail Rekomendasi Teratas")
    
    top_lang, top_score = ranked[0]
    
    # Create tabs for detailed info
    detail_tab1, detail_tab2, detail_tab3 = st.tabs([
        "📊 Analisis Skor", 
        "🗺️ Roadmap Belajar", 
        "📚 Resources"
    ])
    
    with detail_tab1:
        show_score_analysis(top_lang, top_score, rule_scores, ml_scores, explanations, expert)
    
    with detail_tab2:
        display_learning_roadmap(top_lang, industry)
    
    with detail_tab3:
        display_resources(top_lang)
    
    # Comparison table
    st.markdown("---")
    st.markdown("### 📊 Tabel Perbandingan Semua Kandidat")
    display_comparison_table(ranked, expert)
    
    # Chart visualization
    st.markdown("### 📈 Visualisasi Skor")
    chart_data = pd.DataFrame({
        'Bahasa': [lang for lang, _ in ranked],
        'Skor': [score for _, score in ranked]
    })
    st.bar_chart(chart_data.set_index('Bahasa'), use_container_width=True)
    
    # Export option
    st.markdown("---")
    st.markdown("### 💾 Export Hasil")
    
    col1, col2 = st.columns(2)
    with col1:
        text_output = export_to_text(ranked, industry, career_goal, priority, expert)
        st.download_button(
            label="📄 Download sebagai TXT",
            data=text_output,
            file_name="rekomendasi_bahasa_pemrograman.txt",
            mime="text/plain"
        )
    
    with col2:
        if st.button("🔄 Coba Lagi dengan Input Berbeda"):
            st.rerun()


def show_score_analysis(language, total_score, rule_scores, ml_scores, explanations, expert):
    """Menampilkan analisis detail skor"""
    
    st.markdown(f"### Analisis Skor untuk {language}")
    
    # Score breakdown
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Skor Rule-Based",
            f"{rule_scores.get(language, 0):.1f}",
            help="Skor dari sistem pakar berbasis aturan"
        )
    
    with col2:
        st.metric(
            "Skor ML",
            f"{ml_scores.get(language, 0):.1f}",
            help="Skor dari model Naive Bayes"
        )
    
    with col3:
        st.metric(
            "Skor Total",
            f"{total_score:.1f}",
            help="60% Rule-Based + 40% ML"
        )
    
    # Formula explanation
    st.markdown("#### 🧮 Formula Perhitungan:")
    st.code(f"""
Skor Total = (Skor Rule-Based × 0.6) + (Skor ML × 0.4)
           = ({rule_scores.get(language, 0):.1f} × 0.6) + ({ml_scores.get(language, 0):.1f} × 0.4)
           = {total_score:.1f}
    """)
    
    # Explanation dari expert system
    st.markdown("#### 💡 Penjelasan Sistem Pakar:")
    st.markdown(expert.explain_decision(language, rule_scores, explanations))
    
    # ML explanation
    st.markdown("#### 🤖 Penjelasan Machine Learning:")
    st.markdown(ml_scores and f"Model Naive Bayes memberikan probabilitas **{ml_scores.get(language, 0):.1f}%** "
                f"bahwa {language} cocok untuk kebutuhan Anda berdasarkan data industri historis.")


def show_about_page():
    """Halaman tentang sistem"""
    st.markdown("### 📚 Tentang Sistem Pakar Hybrid")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🎯 Konsep Sistem
        
        Sistem ini menggunakan pendekatan **Hybrid** yang menggabungkan:
        
        1. **Rule-Based Expert System**
           - Menggunakan aturan IF-THEN
           - Berbasis domain knowledge IT
           - Filtering kandidat bahasa
           - Explainable AI
        
        2. **Machine Learning (Naive Bayes)**
           - Probabilistic classification
           - Data-driven scoring
           - Belajar dari data industri
           - Adaptif terhadap tren
        
        #### 🔄 Alur Kerja Sistem
        
        ```
        Input User
            ↓
        Rule-Based Filter → Kandidat Bahasa
            ↓
        ML Scoring → Probabilitas
            ↓
        Hybrid Score (60% Rule + 40% ML)
            ↓
        Ranking & Rekomendasi
        ```
        """)
    
    with col2:
        st.markdown("""
        #### 💡 Keunggulan Hybrid Approach
        
        ✅ **Explainability**: Setiap keputusan dapat dijelaskan  
        ✅ **Data-Driven**: Menggunakan data industri real  
        ✅ **Fleksibel**: Mudah di-update dan maintain  
        ✅ **Akurat**: Kombinasi logic + statistics  
        ✅ **User-Friendly**: Interface sederhana
        
        #### 📊 Dataset
        
        Dataset berisi **46 records** dengan fitur:
        - Industry (5 kategori)
        - Career Goal (4 kategori)
        - Priority (3 kategori)
        - Job Demand, Learning Curve, Salary, Community Support
        - Target: 7 bahasa pemrograman
        
        #### 🎓 Tujuan Akademik
        
        Sistem ini dikembangkan sebagai implementasi dari:
        - Artificial Intelligence
        - Expert Systems
        - Machine Learning
        - Software Engineering
        """)
    
    st.markdown("---")
    
    # Technical details
    with st.expander("🔧 Detail Teknis Implementation"):
        st.markdown("""
        **Rule-Based Expert System:**
        - Forward Chaining inference
        - 4 Rule Sets (Industry, Career, Priority, Complexity)
        - Scoring mechanism 0-100
        
        **Machine Learning:**
        - Algorithm: Multinomial Naive Bayes
        - Features: 7 categorical features
        - Training: Supervised learning
        - Output: Probability distribution
        
        **Tech Stack:**
        - Python 3.8+
        - Streamlit (Web Framework)
        - Scikit-learn (ML)
        - Pandas (Data Processing)
        
        **Deployment:**
        - Streamlit Community Cloud
        - GitHub Repository
        - Automatic CI/CD
        """)
    
    with st.expander("📖 Referensi & Sumber"):
        st.markdown("""
        **Referensi Akademik:**
        - Russell & Norvig - Artificial Intelligence: A Modern Approach
        - Expert Systems: Principles and Programming
        - Pattern Recognition and Machine Learning
        
        **Data Sources:**
        - JobStreet Indonesia job postings (2024)
        - LinkedIn Salary Insights
        - Stack Overflow Developer Survey 2024
        - GitHub Technology Trends
        
        **Community Resources:**
        - Python.org, MDN Web Docs
        - Kaggle Datasets
        - Developer Roadmaps
        """)


if __name__ == "__main__":
    main()