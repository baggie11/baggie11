<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bagavati Narayanan - Developer Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            animation: fadeInUp 1s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-section {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="25" cy="75" r="1" fill="white" opacity="0.05"/><circle cx="75" cy="25" r="1" fill="white" opacity="0.05"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            pointer-events: none;
        }

        .profile-header {
            position: relative;
            z-index: 1;
        }

        .profile-title {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #fff, #a8edea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s ease-in-out infinite;
        }

        @keyframes shimmer {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }

        .profile-subtitle {
            font-size: 1.3rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }

        .social-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50px;
            color: white;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .social-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            border-color: rgba(255, 255, 255, 0.5);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .about-section {
            padding: 50px 40px;
            background: white;
        }

        .section-title {
            font-size: 2.5rem;
            color: #2a5298;
            margin-bottom: 30px;
            text-align: center;
            position: relative;
        }

        .section-title::after {
            content: '';
            width: 80px;
            height: 4px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 2px;
        }

        .about-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .about-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .about-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .about-card:hover::before {
            opacity: 1;
        }

        .about-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .about-card h3 {
            color: #2a5298;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }

        .about-card ul {
            list-style: none;
        }

        .about-card li {
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
        }

        .about-card li::before {
            content: '→';
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }

        .tech-section {
            padding: 50px 40px;
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        }

        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }

        .tech-card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }

        .tech-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
            border-color: #667eea;
        }

        .tech-icon {
            width: 50px;
            height: 50px;
            margin: 0 auto 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: white;
            font-size: 1.2rem;
        }

        .tech-name {
            font-weight: 600;
            color: #2a5298;
        }

        .stats-section {
            padding: 50px 40px;
            background: white;
            text-align: center;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
            transition: transform 0.3s ease;
        }

        .stat-card:hover {
            transform: scale(1.05);
        }

        .stat-placeholder {
            width: 100%;
            height: 200px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 15px;
            font-size: 1.1rem;
        }

        .floating-elements {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
            pointer-events: none;
        }

        .floating-element {
            position: absolute;
            width: 20px;
            height: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }

        .floating-element:nth-child(1) {
            top: 20%;
            left: 10%;
            animation-delay: 0s;
        }

        .floating-element:nth-child(2) {
            top: 60%;
            left: 80%;
            animation-delay: 2s;
        }

        .floating-element:nth-child(3) {
            top: 80%;
            left: 20%;
            animation-delay: 4s;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0px) rotate(0deg);
                opacity: 0.7;
            }
            50% {
                transform: translateY(-20px) rotate(180deg);
                opacity: 1;
            }
        }

        @media (max-width: 768px) {
            .hero-section {
                padding: 40px 20px;
            }

            .profile-title {
                font-size: 2.5rem;
            }

            .about-section, .tech-section, .stats-section {
                padding: 30px 20px;
            }

            .social-links {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero Section -->
        <div class="hero-section">
            <div class="floating-elements">
                <div class="floating-element"></div>
                <div class="floating-element"></div>
                <div class="floating-element"></div>
            </div>
            
            <div class="profile-header">
                <h1 class="profile-title">👋 Bagavati Narayanan</h1>
                <p class="profile-subtitle">A passionate <strong>coding enthusiast</strong> from Chennai 🚀</p>
                
                <div class="social-links">
                    <a href="https://www.linkedin.com/in/bagavati-narayanan-98484b292/" class="social-btn">
                        💼 LinkedIn
                    </a>
                    <a href="mailto:bagavati2310098@ssn.edu.in" class="social-btn">
                        ✉️ Email Me
                    </a>
                </div>
            </div>
        </div>

        <!-- About Section -->
        <div class="about-section">
            <h2 class="section-title">About Me</h2>
            <div class="about-grid">
                <div class="about-card">
                    <h3>🤝 Collaboration</h3>
                    <ul>
                        <li>Web Development</li>
                        <li>Machine Learning</li>
                        <li>Deep Learning</li>
                        <li>Large Language Models</li>
                    </ul>
                </div>
                
                <div class="about-card">
                    <h3>💡 Expertise</h3>
                    <ul>
                        <li>Python & Java Development</li>
                        <li>MERN Stack</li>
                        <li>Django & Flask</li>
                        <li>FastAPI & Langchain</li>
                    </ul>
                </div>
                
                <div class="about-card">
                    <h3>📍 Location & Contact</h3>
                    <ul>
                        <li>Based in Chennai, India</li>
                        <li>Available for collaboration</li>
                        <li>Open to new opportunities</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Tech Stack Section -->
        <div class="tech-section">
            <h2 class="section-title">🧰 Tech Stack</h2>
            <div class="tech-grid">
                <div class="tech-card">
                    <div class="tech-icon">J</div>
                    <div class="tech-name">Java</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🐍</div>
                    <div class="tech-name">Python</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">JS</div>
                    <div class="tech-name">JavaScript</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">⚛️</div>
                    <div class="tech-name">React</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">N</div>
                    <div class="tech-name">Next.js</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">V</div>
                    <div class="tech-name">Vue.js</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🟢</div>
                    <div class="tech-name">Node.js</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">F</div>
                    <div class="tech-name">Flask</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🚀</div>
                    <div class="tech-name">FastAPI</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🐼</div>
                    <div class="tech-name">Pandas</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">📊</div>
                    <div class="tech-name">NumPy</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🤖</div>
                    <div class="tech-name">PyTorch</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🔗</div>
                    <div class="tech-name">LangChain</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🍃</div>
                    <div class="tech-name">MongoDB</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🔥</div>
                    <div class="tech-name">Firebase</div>
                </div>
                <div class="tech-card">
                    <div class="tech-icon">🐬</div>
                    <div class="tech-name">MySQL</div>
                </div>
            </div>
        </div>

        <!-- GitHub Stats Section -->
        <div class="stats-section">
            <h2 class="section-title">📈 GitHub Stats</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-placeholder">
                        GitHub Stats<br>
                        <small>Visit your actual GitHub profile to see live stats</small>
                    </div>
                    <h3>Overall Statistics</h3>
                </div>
                
                <div class="stat-card">
                    <div class="stat-placeholder">
                        Top Languages<br>
                        <small>Most used programming languages</small>
                    </div>
                    <h3>Language Distribution</h3>
                </div>
                
                <div class="stat-card">
                    <div class="stat-placeholder">
                        Contribution Graph<br>
                        <small>Activity over time</small>
                    </div>
                    <h3>Activity Overview</h3>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
