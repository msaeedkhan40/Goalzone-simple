"""
GoalZone – Flask Backend (Simple / No Docker)
Serves the API and static frontend from a single process.
Uses SQLite so no database installation is required.

Run:
    pip install flask flask-cors
    python app.py

Then open:  http://localhost:5000
"""

import os
import sqlite3
from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# ── App setup ─────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
FRONTEND  = os.path.join(BASE_DIR, '..', 'frontend')
DB_PATH   = os.path.join(BASE_DIR, 'goalzone.db')

app = Flask(__name__, static_folder=FRONTEND, static_url_path='')
CORS(app)

# ── Database ──────────────────────────────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create the contact_messages table if it doesn't exist."""
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contact_messages (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT NOT NULL,
                email      TEXT NOT NULL,
                message    TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        conn.commit()
    print("✅ Database ready:", DB_PATH)

# ── Sample data ───────────────────────────────────────────────────────────────
MATCHES = [
    {
        "id": 1,
        "home_team": "Manchester City",
        "away_team": "Arsenal",
        "home_score": 2, "away_score": 1,
        "date": "2025-11-20", "time": "20:00",
        "status": "upcoming",
        "venue": "Etihad Stadium",
        "competition": "Premier League",
        "home_logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
    },
    {
        "id": 2,
        "home_team": "Real Madrid",
        "away_team": "Barcelona",
        "home_score": 3, "away_score": 2,
        "date": "2025-11-22", "time": "21:00",
        "status": "upcoming",
        "venue": "Santiago Bernabéu",
        "competition": "La Liga",
        "home_logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
    },
    {
        "id": 3,
        "home_team": "Bayern Munich",
        "away_team": "Borussia Dortmund",
        "home_score": 4, "away_score": 0,
        "date": "2025-11-23", "time": "17:30",
        "status": "upcoming",
        "venue": "Allianz Arena",
        "competition": "Bundesliga",
        "home_logo": "https://upload.wikimedia.org/wikipedia/commons/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282002%E2%80%932017%29.svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/commons/6/67/Borussia_Dortmund_logo.svg",
    },
    {
        "id": 4,
        "home_team": "Liverpool",
        "away_team": "Chelsea",
        "home_score": 1, "away_score": 1,
        "date": "2025-11-25", "time": "19:45",
        "status": "upcoming",
        "venue": "Anfield",
        "competition": "Premier League",
        "home_logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
    },
    {
        "id": 5,
        "home_team": "PSG",
        "away_team": "Marseille",
        "home_score": 2, "away_score": 0,
        "date": "2025-11-27", "time": "21:00",
        "status": "upcoming",
        "venue": "Parc des Princes",
        "competition": "Ligue 1",
        "home_logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Olympique_Marseille_logo.svg",
    },
    {
        "id": 6,
        "home_team": "Juventus",
        "away_team": "Inter Milan",
        "home_score": 0, "away_score": 2,
        "date": "2025-11-28", "time": "20:45",
        "status": "upcoming",
        "venue": "Allianz Stadium",
        "competition": "Serie A",
        "home_logo": "https://upload.wikimedia.org/wikipedia/commons/1/15/Juventus_FC_2017_logo.svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/commons/0/05/FC_Internazionale_Milano_2021.svg",
    },
]

TEAMS = [
    {
        "id": 1,
        "name": "Manchester City",
        "country": "England",
        "logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
        "founded": 1880,
        "stadium": "Etihad Stadium",
        "description": "One of England's most successful clubs, Manchester City have dominated the Premier League era with their fluid, attacking football under Pep Guardiola.",
    },
    {
        "id": 2,
        "name": "Real Madrid",
        "country": "Spain",
        "logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        "founded": 1902,
        "stadium": "Santiago Bernabéu",
        "description": "The most decorated club in Champions League history, Real Madrid are synonymous with European glory and world-class galáctico signings.",
    },
    {
        "id": 3,
        "name": "Bayern Munich",
        "country": "Germany",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282002%E2%80%932017%29.svg",
        "founded": 1900,
        "stadium": "Allianz Arena",
        "description": "Germany's dominant force, Bayern Munich have been Bundesliga champions for over a decade and regular contenders for European honours.",
    },
    {
        "id": 4,
        "name": "Liverpool",
        "country": "England",
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
        "founded": 1892,
        "stadium": "Anfield",
        "description": "With six European Cups, Liverpool are England's most successful club on the continental stage, famous for their electric atmosphere at Anfield.",
    },
    {
        "id": 5,
        "name": "Barcelona",
        "country": "Spain",
        "logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
        "founded": 1899,
        "stadium": "Camp Nou",
        "description": "Known for their beautiful tiki-taka style, Barcelona produced some of the finest footballers of all time including Messi, Xavi and Iniesta.",
    },
    {
        "id": 6,
        "name": "PSG",
        "country": "France",
        "logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg",
        "founded": 1970,
        "stadium": "Parc des Princes",
        "description": "Paris Saint-Germain are France's biggest club, backed by Qatari investment and home to global superstars aiming for Champions League glory.",
    },
]

NEWS = [
    {
        "id": 1,
        "title": "Manchester City's Tactical Revolution Under Guardiola",
        "category": "Analysis",
        "date": "2025-11-15",
        "image": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80",
        "description": "Pep Guardiola has transformed Manchester City into a machine of relentless pressing and intricate passing. We break down the tactical evolution that has made them the Premier League's most dominant side in a generation.",
        "author": "James Collins",
    },
    {
        "id": 2,
        "title": "El Clásico Preview: Real Madrid vs Barcelona",
        "category": "Preview",
        "date": "2025-11-17",
        "image": "https://images.unsplash.com/photo-1543326727-cf6c39e8f84c?w=800&q=80",
        "description": "The world stops when Real Madrid and Barcelona meet. This season's El Clásico promises fireworks as both sides are locked in a tight title race. Here's everything you need to know.",
        "author": "Sofia Martinez",
    },
    {
        "id": 3,
        "title": "Champions League: Who Are the Favourites This Season?",
        "category": "Champions League",
        "date": "2025-11-14",
        "image": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80",
        "description": "With the group stages wrapped up, the knockout rounds are set. We analyse the form, squad depth and tactical advantages of the leading contenders for Europe's biggest prize.",
        "author": "Luca Bianchi",
    },
    {
        "id": 4,
        "title": "Rising Stars: The Young Players Who Will Define 2026",
        "category": "Features",
        "date": "2025-11-13",
        "image": "https://images.unsplash.com/photo-1575361204480-aadea25e6e68?w=800&q=80",
        "description": "Every season a new generation of talent emerges. From the streets of Madrid to the academies of London, we spotlight five young players set to make 2026 their breakthrough year.",
        "author": "Priya Sharma",
    },
    {
        "id": 5,
        "title": "The Science of Set Pieces: How Teams Win From Dead Balls",
        "category": "Tactics",
        "date": "2025-11-11",
        "image": "https://images.unsplash.com/photo-1546961342-ea5f71aa193e?w=800&q=80",
        "description": "Nearly a third of all goals in top-level football now come from set pieces. We explore the growing importance of corner kick routines and the data-driven coaching revolution changing the game.",
        "author": "David Okafor",
    },
]

# ── API Routes ────────────────────────────────────────────────────────────────

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'timestamp': datetime.utcnow().isoformat()})

@app.route('/api/matches')
def get_matches():
    return jsonify({'matches': MATCHES, 'total': len(MATCHES)})

@app.route('/api/teams')
def get_teams():
    return jsonify({'teams': TEAMS, 'total': len(TEAMS)})

@app.route('/api/news')
def get_news():
    return jsonify({'news': NEWS, 'total': len(NEWS)})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    name    = (data.get('name') or '').strip()
    email   = (data.get('email') or '').strip()
    message = (data.get('message') or '').strip()

    if not name or not email or not message:
        return jsonify({'error': 'All fields are required'}), 400

    try:
        with get_db() as conn:
            conn.execute(
                'INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)',
                (name, email, message)
            )
            conn.commit()
        print(f"📬 New message from {name} <{email}>")
        return jsonify({'success': True, 'message': 'Thank you! Your message has been received.'}), 201
    except Exception as e:
        print('DB error:', e)
        return jsonify({'error': 'Could not save your message. Please try again.'}), 500

# ── Serve frontend pages ──────────────────────────────────────────────────────

@app.route('/')
@app.route('/index.html')
def home():
    return send_from_directory(FRONTEND, 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(FRONTEND, filename)

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    print("\n⚽  GoalZone is running!")
    print("   Open: http://localhost:5000\n")
    app.run(debug=True, port=5000)
