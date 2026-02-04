"""
Rule-Based Expert System
Sistem pakar berbasis aturan IF-THEN untuk filtering bahasa pemrograman
"""

class ExpertSystem:
    def __init__(self):
        # KNOWLEDGE BASE - Rule Set 1: Bidang Industri
        self.rules_industry = {
            "Web Development": {
                "languages": ["JavaScript", "Python", "PHP"],
                "reasoning": "Bahasa dengan framework web populer dan banyak lowongan"
            },
            "Data Science": {
                "languages": ["Python"],
                "reasoning": "Standar industri untuk data analysis, ML, dan AI"
            },
            "Mobile Development": {
                "languages": ["JavaScript", "Kotlin", "Java"],
                "reasoning": "React Native (JS), Flutter (JS), dan Android native"
            },
            "Backend Development": {
                "languages": ["Python", "JavaScript", "Java", "Golang", "PHP"],
                "reasoning": "Bahasa server-side yang banyak digunakan di industri"
            },
            "Game Development": {
                "languages": ["C#", "JavaScript"],
                "reasoning": "Unity (C#) dan HTML5 games (JavaScript)"
            }
        }
        
        # Rule Set 2: Tujuan Karier
        self.rules_career_goal = {
            "Kerja cepat": {
                "boost": ["JavaScript", "Python", "PHP", "Java"],
                "score": 15,
                "reasoning": "Banyak lowongan entry-level di job portal"
            },
            "Magang": {
                "boost": ["Python", "JavaScript", "Java", "Kotlin"],
                "score": 15,
                "reasoning": "Populer di program magang tech companies"
            },
            "Freelance": {
                "boost": ["JavaScript", "PHP", "Python"],
                "score": 15,
                "reasoning": "Banyak project web development dan automation"
            },
            "Startup": {
                "boost": ["JavaScript", "Python", "Golang"],
                "score": 15,
                "reasoning": "Tech stack modern yang digunakan startup"
            }
        }
        
        # Rule Set 3: Prioritas Pemula
        self.rules_beginner_priority = {
            "Mudah dipelajari": {
                "preferred": ["Python", "JavaScript"],
                "score": 20,
                "avoid": ["Java", "C#", "Golang"],
                "reasoning": "Syntax sederhana, banyak tutorial pemula"
            },
            "Banyak lowongan": {
                "preferred": ["JavaScript", "Python", "Java", "PHP"],
                "score": 20,
                "reasoning": "Permintaan industri tinggi di Indonesia"
            },
            "Gaji tinggi": {
                "preferred": ["Python", "JavaScript", "Golang"],
                "score": 20,
                "reasoning": "Tren gaji entry-level 2024-2025"
            }
        }
        
        # Rule Set 4: Tingkat Kompleksitas untuk Pemula
        self.beginner_complexity = {
            "Sangat Cocok": {
                "languages": ["Python", "JavaScript"],
                "score": 25,
                "reasoning": "Syntax intuitif, curve belajar landai"
            },
            "Cocok": {
                "languages": ["PHP", "Kotlin"],
                "score": 15,
                "reasoning": "Cukup mudah dengan dokumentasi baik"
            },
            "Menengah": {
                "languages": ["Java", "C#"],
                "score": 10,
                "reasoning": "Butuh pemahaman OOP yang solid"
            },
            "Perlu Dedikasi": {
                "languages": ["Golang"],
                "score": 5,
                "reasoning": "Konsep concurrent programming perlu waktu"
            }
        }
    
    def infer(self, industry, career_goal, priority):
        """
        Forward Chaining Inference Engine
        Menerapkan aturan IF-THEN secara berurutan
        
        Args:
            industry: Bidang industri yang diminati
            career_goal: Tujuan karier
            priority: Prioritas sebagai pemula
            
        Returns:
            (candidate_languages, scores, explanations)
        """
        candidate_languages = set()
        scores = {}
        explanations = {}
        
        # RULE 1: Filter berdasarkan INDUSTRI (Primary Filter)
        if industry in self.rules_industry:
            langs = self.rules_industry[industry]["languages"]
            candidate_languages.update(langs)
            explanations["industry"] = self.rules_industry[industry]["reasoning"]
            
            # Inisialisasi skor dasar
            for lang in langs:
                scores[lang] = 10  # Base score
        
        # RULE 2: Boost berdasarkan TUJUAN KARIER
        if career_goal in self.rules_career_goal:
            boost_langs = self.rules_career_goal[career_goal]["boost"]
            boost_score = self.rules_career_goal[career_goal]["score"]
            
            for lang in boost_langs:
                if lang in candidate_languages:
                    scores[lang] = scores.get(lang, 0) + boost_score
            
            explanations["career_goal"] = self.rules_career_goal[career_goal]["reasoning"]
        
        # RULE 3: Boost berdasarkan PRIORITAS PEMULA
        if priority in self.rules_beginner_priority:
            preferred = self.rules_beginner_priority[priority]["preferred"]
            pref_score = self.rules_beginner_priority[priority]["score"]
            
            for lang in preferred:
                if lang in candidate_languages:
                    scores[lang] = scores.get(lang, 0) + pref_score
            
            explanations["priority"] = self.rules_beginner_priority[priority]["reasoning"]
        
        # RULE 4: Adjustment berdasarkan KOMPLEKSITAS PEMULA
        for complexity_level, data in self.beginner_complexity.items():
            for lang in data["languages"]:
                if lang in candidate_languages:
                    scores[lang] = scores.get(lang, 0) + data["score"]
        
        # Normalisasi skor ke range 0-100
        if scores:
            max_score = max(scores.values())
            if max_score > 0:
                for lang in scores:
                    scores[lang] = (scores[lang] / max_score) * 100
        
        return candidate_languages, scores, explanations
    
    def get_language_info(self, language, industry):
        """
        Mendapatkan informasi detail tentang bahasa pemrograman
        
        Args:
            language: Nama bahasa pemrograman
            industry: Bidang industri
            
        Returns:
            Dictionary dengan informasi bahasa
        """
        language_info = {
            "Python": {
                "description": "Bahasa pemrograman serbaguna dengan syntax yang mudah dipahami",
                "use_cases": {
                    "Web Development": "Django, Flask untuk backend web application",
                    "Data Science": "NumPy, Pandas, Scikit-learn, TensorFlow",
                    "Backend Development": "FastAPI, Django REST Framework",
                    "Game Development": "Pygame untuk game 2D sederhana"
                },
                "pros": ["Syntax sederhana", "Banyak library", "Komunitas besar", "Cocok pemula"],
                "cons": ["Lebih lambat dari compiled language", "Mobile development terbatas"],
                "avg_salary": "Rp 6-12 juta/bulan (entry-level)",
                "learning_time": "3-6 bulan untuk dasar",
                "resources": [
                    "Codecademy Python Course",
                    "Python.org Documentation",
                    "Real Python Tutorials"
                ]
            },
            "JavaScript": {
                "description": "Bahasa untuk web development, frontend dan backend",
                "use_cases": {
                    "Web Development": "React, Vue, Angular untuk frontend; Node.js untuk backend",
                    "Mobile Development": "React Native untuk cross-platform mobile",
                    "Backend Development": "Express.js, Nest.js",
                    "Game Development": "Phaser, Three.js untuk HTML5 games"
                },
                "pros": ["Essential untuk web", "Full-stack capability", "Ekosistem npm besar"],
                "cons": ["Banyak framework berubah cepat", "Async programming butuh pemahaman"],
                "avg_salary": "Rp 7-13 juta/bulan (entry-level)",
                "learning_time": "4-7 bulan untuk dasar + framework",
                "resources": [
                    "MDN Web Docs",
                    "JavaScript.info",
                    "FreeCodeCamp"
                ]
            },
            "PHP": {
                "description": "Bahasa server-side untuk web development",
                "use_cases": {
                    "Web Development": "Laravel, CodeIgniter untuk web backend",
                    "Backend Development": "WordPress, API development"
                },
                "pros": ["Mudah deploy", "Banyak hosting support", "WordPress ecosystem"],
                "cons": ["Reputasi legacy code", "Kurang populer di startup baru"],
                "avg_salary": "Rp 5-10 juta/bulan (entry-level)",
                "learning_time": "3-5 bulan untuk dasar",
                "resources": [
                    "PHP.net Documentation",
                    "Laravel Documentation",
                    "Laracasts"
                ]
            },
            "Java": {
                "description": "Bahasa OOP yang mature untuk enterprise dan Android",
                "use_cases": {
                    "Mobile Development": "Android native development",
                    "Backend Development": "Spring Boot untuk enterprise backend"
                },
                "pros": ["Mature ecosystem", "Banyak lowongan enterprise", "Strong typing"],
                "cons": ["Verbose syntax", "Curve belajar lebih curam untuk pemula"],
                "avg_salary": "Rp 7-14 juta/bulan (entry-level)",
                "learning_time": "5-8 bulan untuk dasar + framework",
                "resources": [
                    "Oracle Java Tutorials",
                    "Head First Java",
                    "Udemy Java Courses"
                ]
            },
            "Kotlin": {
                "description": "Modern language untuk Android development",
                "use_cases": {
                    "Mobile Development": "Android native (officially supported)",
                    "Backend Development": "Ktor framework"
                },
                "pros": ["Modern syntax", "Interop dengan Java", "Official Android language"],
                "cons": ["Lebih niche", "Komunitas lebih kecil dari Java"],
                "avg_salary": "Rp 7-13 juta/bulan (entry-level)",
                "learning_time": "4-6 bulan (jika sudah tahu Java)",
                "resources": [
                    "Kotlin Official Docs",
                    "Android Kotlin Fundamentals",
                    "Kotlin Koans"
                ]
            },
            "C#": {
                "description": "Bahasa Microsoft untuk game dan enterprise",
                "use_cases": {
                    "Game Development": "Unity game engine",
                    "Backend Development": ".NET Core untuk web services"
                },
                "pros": ["Unity ecosystem", "Strong typing", "Good tooling (Visual Studio)"],
                "cons": ["Lebih terbatas di luar Windows ecosystem", "Unity butuh dedikasi"],
                "avg_salary": "Rp 7-13 juta/bulan (entry-level)",
                "learning_time": "5-7 bulan untuk dasar + Unity",
                "resources": [
                    "Microsoft C# Documentation",
                    "Unity Learn Platform",
                    "C# Programming Yellow Book"
                ]
            },
            "Golang": {
                "description": "Modern language untuk backend performa tinggi",
                "use_cases": {
                    "Backend Development": "Microservices, API, cloud services"
                },
                "pros": ["Performa tinggi", "Concurrency built-in", "Compile cepat"],
                "cons": ["Lebih kompleks untuk pemula", "Lowongan entry-level lebih sedikit"],
                "avg_salary": "Rp 8-15 juta/bulan (entry-level, tapi sedikit posisi)",
                "learning_time": "6-9 bulan untuk mahir",
                "resources": [
                    "Go by Example",
                    "Tour of Go",
                    "Go Official Documentation"
                ]
            }
        }
        
        info = language_info.get(language, {})
        
        # Tambahkan use case spesifik untuk industri
        if info and industry in info.get("use_cases", {}):
            info["industry_specific"] = info["use_cases"][industry]
        
        return info
    
    def explain_decision(self, language, scores, explanations):
        """
        Menjelaskan keputusan sistem pakar
        
        Args:
            language: Bahasa yang direkomendasikan
            scores: Dictionary skor
            explanations: Dictionary penjelasan
            
        Returns:
            String penjelasan lengkap
        """
        explanation = f"**Mengapa {language}?**\n\n"
        explanation += f"Skor Sistem Pakar: {scores.get(language, 0):.1f}/100\n\n"
        
        explanation += "**Alasan Rekomendasi:**\n"
        for key, reason in explanations.items():
            explanation += f"- {reason}\n"
        
        return explanation