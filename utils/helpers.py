"""
Utility Functions
Helper functions untuk visualisasi dan formatting
"""

import pandas as pd
import streamlit as st


def format_percentage(value):
    """Format nilai ke persentase"""
    return f"{value:.1f}%"


def get_language_emoji(language):
    """Mendapatkan emoji untuk setiap bahasa"""
    emojis = {
        "Python": "🐍",
        "JavaScript": "🟨",
        "PHP": "🐘",
        "Java": "☕",
        "Kotlin": "🅺",
        "C#": "#️⃣",
        "Golang": "🔷"
    }
    return emojis.get(language, "💻")


def get_difficulty_color(language):
    """Mendapatkan warna berdasarkan tingkat kesulitan"""
    easy = ["Python", "JavaScript", "PHP"]
    medium = ["Kotlin"]
    hard = ["Java", "C#", "Golang"]
    
    if language in easy:
        return "green"
    elif language in medium:
        return "orange"
    else:
        return "red"


def get_difficulty_label(language):
    """Label tingkat kesulitan"""
    easy = ["Python", "JavaScript", "PHP"]
    medium = ["Kotlin"]
    hard = ["Java", "C#", "Golang"]
    
    if language in easy:
        return "⭐ Mudah untuk Pemula"
    elif language in medium:
        return "⭐⭐ Sedang"
    else:
        return "⭐⭐⭐ Butuh Dedikasi"


def create_score_dataframe(ranked_languages):
    """
    Membuat DataFrame untuk visualisasi skor
    
    Args:
        ranked_languages: List of tuples (language, score)
        
    Returns:
        pandas DataFrame
    """
    df = pd.DataFrame(ranked_languages, columns=['Bahasa', 'Skor'])
    df['Emoji'] = df['Bahasa'].apply(get_language_emoji)
    return df


def display_language_card(language, score, rank, info, industry):
    """
    Menampilkan card informasi bahasa pemrograman
    
    Args:
        language: Nama bahasa
        score: Skor total
        rank: Ranking
        info: Dictionary informasi bahasa
        industry: Bidang industri
    """
    emoji = get_language_emoji(language)
    difficulty = get_difficulty_label(language)
    
    # Card header
    st.markdown(f"### {rank}. {emoji} {language}")
    
    # Skor
    col1, col2 = st.columns([2, 1])
    with col1:
        st.progress(score / 100)
    with col2:
        st.metric("Skor", f"{score:.1f}/100")
    
    # Tingkat kesulitan
    st.markdown(f"**Tingkat Kesulitan:** {difficulty}")
    
    # Deskripsi
    if info:
        st.markdown(f"**Tentang {language}:**")
        st.write(info.get('description', 'N/A'))
        
        # Use case spesifik industri
        if 'industry_specific' in info:
            st.markdown(f"**Untuk {industry}:**")
            st.info(info['industry_specific'])
        
        # Pros
        if 'pros' in info and info['pros']:
            st.markdown("**Keunggulan:**")
            for pro in info['pros'][:3]:  # Top 3
                st.markdown(f"✅ {pro}")
        
        # Learning info
        col3, col4 = st.columns(2)
        with col3:
            if 'learning_time' in info:
                st.markdown(f"⏱️ **Waktu Belajar:** {info['learning_time']}")
        with col4:
            if 'avg_salary' in info:
                st.markdown(f"💰 **Salary:** {info['avg_salary']}")
    
    st.divider()


def display_comparison_table(ranked_languages, expert_system):
    """
    Menampilkan tabel perbandingan bahasa
    
    Args:
        ranked_languages: List of (language, score)
        expert_system: Instance ExpertSystem
    """
    comparison_data = []
    
    for lang, score in ranked_languages:
        info = expert_system.get_language_info(lang, "General")
        comparison_data.append({
            'Bahasa': f"{get_language_emoji(lang)} {lang}",
            'Skor': f"{score:.1f}",
            'Kesulitan': get_difficulty_label(lang).split()[0],
            'Waktu Belajar': info.get('learning_time', 'N/A') if info else 'N/A',
            'Gaji Entry': info.get('avg_salary', 'N/A') if info else 'N/A'
        })
    
    df = pd.DataFrame(comparison_data)
    st.table(df)


def display_learning_roadmap(language, industry):
    """
    Menampilkan roadmap belajar untuk bahasa tertentu
    
    Args:
        language: Nama bahasa
        industry: Bidang industri
    """
    roadmaps = {
        "Python": {
            "Web Development": [
                "1️⃣ Dasar Python (2-3 bulan): Variables, loops, functions, OOP",
                "2️⃣ Web Framework (2-3 bulan): Flask atau Django basics",
                "3️⃣ Database (1-2 bulan): SQL, PostgreSQL/MySQL",
                "4️⃣ Project Portfolio: Buat 2-3 web app sederhana"
            ],
            "Data Science": [
                "1️⃣ Dasar Python (2-3 bulan): Syntax, data structures",
                "2️⃣ Data Analysis (2 bulan): NumPy, Pandas",
                "3️⃣ Visualization (1 bulan): Matplotlib, Seaborn",
                "4️⃣ Machine Learning (2-3 bulan): Scikit-learn basics"
            ],
            "Backend Development": [
                "1️⃣ Dasar Python (2-3 bulan): Core concepts",
                "2️⃣ Framework (2 bulan): FastAPI atau Django",
                "3️⃣ API Development (1-2 bulan): REST API, authentication",
                "4️⃣ Deployment (1 bulan): Docker, cloud basics"
            ]
        },
        "JavaScript": {
            "Web Development": [
                "1️⃣ HTML/CSS (1-2 bulan): Fundamental web",
                "2️⃣ JavaScript Basics (2-3 bulan): ES6+, DOM manipulation",
                "3️⃣ Frontend Framework (2-3 bulan): React atau Vue",
                "4️⃣ Backend (2 bulan): Node.js + Express"
            ],
            "Mobile Development": [
                "1️⃣ JavaScript Fundamentals (2-3 bulan)",
                "2️⃣ React Basics (2 bulan): Components, state, props",
                "3️⃣ React Native (2-3 bulan): Mobile development",
                "4️⃣ Mobile Project: Buat aplikasi mobile sederhana"
            ]
        },
        # Tambahkan roadmap untuk bahasa lain...
    }
    
    roadmap = roadmaps.get(language, {}).get(industry, [
        "1️⃣ Pelajari syntax dasar (2-3 bulan)",
        "2️⃣ Praktik dengan project kecil (2 bulan)",
        "3️⃣ Pelajari framework populer (2-3 bulan)",
        "4️⃣ Buat portfolio project (1-2 bulan)"
    ])
    
    st.markdown("### 🗺️ Roadmap Belajar")
    for step in roadmap:
        st.markdown(step)


def display_resources(language):
    """
    Menampilkan resources belajar
    
    Args:
        language: Nama bahasa
    """
    resources = {
        "Python": [
            ("📚 Python.org - Official Tutorial", "https://docs.python.org/3/tutorial/"),
            ("🎥 Corey Schafer YouTube", "https://www.youtube.com/user/schafer5"),
            ("💻 Real Python", "https://realpython.com/"),
            ("🏫 Codecademy Python", "https://www.codecademy.com/learn/learn-python-3")
        ],
        "JavaScript": [
            ("📚 MDN Web Docs", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"),
            ("🎥 FreeCodeCamp", "https://www.freecodecamp.org/"),
            ("💻 JavaScript.info", "https://javascript.info/"),
            ("🏫 The Odin Project", "https://www.theodinproject.com/")
        ],
        "PHP": [
            ("📚 PHP.net Documentation", "https://www.php.net/manual/en/"),
            ("🎥 Traversy Media YouTube", "https://www.youtube.com/user/TechGuyWeb"),
            ("💻 Laracasts (Laravel)", "https://laracasts.com/"),
            ("🏫 PHP The Right Way", "https://phptherightway.com/")
        ],
        "Java": [
            ("📚 Oracle Java Tutorials", "https://docs.oracle.com/javase/tutorial/"),
            ("🎥 Programming with Mosh", "https://www.youtube.com/user/programmingwithmosh"),
            ("💻 Java Point", "https://www.javatpoint.com/java-tutorial"),
            ("🏫 Udemy - Java Masterclass", "https://www.udemy.com/")
        ]
    }
    
    resource_list = resources.get(language, [
        ("📚 Official Documentation", "#"),
        ("🎥 YouTube Tutorials", "https://www.youtube.com/"),
        ("💻 Online Courses", "https://www.udemy.com/"),
        ("🏫 Interactive Learning", "https://www.codecademy.com/")
    ])
    
    st.markdown("### 📖 Resources Belajar")
    for title, url in resource_list:
        st.markdown(f"- [{title}]({url})")


def export_to_text(ranked_languages, industry, career_goal, priority, expert_system):
    """
    Export hasil rekomendasi ke format text
    
    Returns:
        String dengan format text lengkap
    """
    output = "="*60 + "\n"
    output += "HASIL REKOMENDASI BAHASA PEMROGRAMAN\n"
    output += "Sistem Pakar Hybrid (Rule-Based + Machine Learning)\n"
    output += "="*60 + "\n\n"
    
    output += f"Input Anda:\n"
    output += f"- Bidang Industri: {industry}\n"
    output += f"- Tujuan Karier: {career_goal}\n"
    output += f"- Prioritas: {priority}\n\n"
    
    output += "="*60 + "\n"
    output += "TOP 3 REKOMENDASI:\n"
    output += "="*60 + "\n\n"
    
    for i, (lang, score) in enumerate(ranked_languages[:3], 1):
        emoji = get_language_emoji(lang)
        info = expert_system.get_language_info(lang, industry)
        
        output += f"{i}. {emoji} {lang} - Skor: {score:.1f}/100\n"
        output += f"   {'-'*55}\n"
        if info:
            output += f"   {info.get('description', '')}\n\n"
            if 'industry_specific' in info:
                output += f"   Untuk {industry}:\n"
                output += f"   {info['industry_specific']}\n\n"
        output += "\n"
    
    output += "="*60 + "\n"
    output += "Terima kasih telah menggunakan sistem rekomendasi kami!\n"
    output += "="*60 + "\n"
    
    return output