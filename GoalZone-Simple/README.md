# ⚽ GoalZone

A modern, responsive football website built with **Flask (Python)**, **SQLite** and **Vanilla JS**.

No Docker, no database server — just Python and a browser.

---

## 📁 Project Structure

```
GoalZone-Simple/
├── frontend/               ← All web pages (HTML/CSS/JS)
│   ├── index.html          ← Home page
│   ├── matches.html        ← Upcoming matches
│   ├── teams.html          ← Football teams
│   ├── news.html           ← News articles
│   ├── contact.html        ← Contact form
│   ├── css/
│   │   └── style.css       ← Dark football-themed stylesheet
│   └── js/
│       ├── main.js         ← Shared utilities
│       ├── matches.js      ← Matches page logic
│       ├── teams.js        ← Teams page logic
│       ├── news.js         ← News page logic
│       └── contact.js      ← Form submission
│
└── backend/
    ├── app.py              ← Flask API + serves the frontend
    └── requirements.txt    ← Python dependencies
```

---

## 🚀 How to Run

### Step 1 – Install Python dependencies

Open a terminal, go to the `backend` folder and run:

```bash
cd GoalZone-Simple/backend

# (Optional but recommended) create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Mac/Linux

# Install Flask
pip install -r requirements.txt
```

### Step 2 – Start the server

```bash
python app.py
```

You should see:

```
✅ Database ready: .../backend/goalzone.db
⚽  GoalZone is running!
   Open: http://localhost:5000
```

### Step 3 – Open the website

Go to **http://localhost:5000** in your browser. That's it! 🎉

---

## 🔌 API Endpoints

| Method | Endpoint       | Description                             |
|--------|----------------|-----------------------------------------|
| GET    | `/api/health`  | Health check                            |
| GET    | `/api/matches` | Returns 6 upcoming matches              |
| GET    | `/api/teams`   | Returns 6 football teams                |
| GET    | `/api/news`    | Returns 5 news articles                 |
| POST   | `/api/contact` | Saves a contact message to SQLite       |

### POST `/api/contact` – example body

```json
{
  "name": "Alex Johnson",
  "email": "alex@example.com",
  "message": "Great website!"
}
```

---

## 💾 Viewing Saved Messages

Contact form submissions are stored in `backend/goalzone.db` (SQLite).

To view them, open a terminal and run:

```bash
# Install sqlite3 CLI if you don't have it, or use DB Browser for SQLite
sqlite3 backend/goalzone.db "SELECT * FROM contact_messages;"
```

Or download the free GUI tool: https://sqlitebrowser.org

---

## 🌐 Pages

| Page          | URL                           | Features                                   |
|---------------|-------------------------------|--------------------------------------------|
| Home          | http://localhost:5000         | Hero, featured matches, teams, news        |
| Matches       | http://localhost:5000/matches.html | 6 upcoming fixtures with scores      |
| Teams         | http://localhost:5000/teams.html   | 6 clubs with logos and descriptions  |
| News          | http://localhost:5000/news.html    | 5 articles with images               |
| Contact       | http://localhost:5000/contact.html | Form → saved to SQLite              |

---

## 🛠️ Tech Stack

| Layer    | Technology               |
|----------|--------------------------|
| Frontend | HTML5, CSS3, Vanilla JS  |
| Backend  | Python 3, Flask          |
| Database | SQLite (built into Python — no install needed!) |

---

## 🔧 Stopping the Server

Press `Ctrl + C` in the terminal to stop Flask.
