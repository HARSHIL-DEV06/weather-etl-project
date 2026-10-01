# 🌦️ Weather ETL Pipeline

A beginner-friendly **ETL (Extract → Transform → Load)** pipeline built in Python that fetches real-time weather data from a public API, cleans and structures it, and stores it into a **PostgreSQL** database.

---

## 📌 Project Overview

This project demonstrates a complete data engineering workflow:

| Stage | What it does |
|-------|-------------|
| **Extract** | Fetches live weather data (temperature, windspeed, timestamp) from the [Open-Meteo API](https://open-meteo.com/) |
| **Transform** | Parses the raw JSON response and extracts only the relevant fields |
| **Load** | Inserts the cleaned, structured data into a PostgreSQL table |

> **Target Location:** Mumbai, India (Latitude: 19.07, Longitude: 72.87)

---

## 🗂️ Project Structure

```
Basic_ETL_Weather/
│
├── main.py          # Pipeline orchestrator — runs all 3 stages in order
├── extract.py       # Stage 1: Fetches raw weather data from the API
├── transform.py     # Stage 2: Cleans and structures the raw JSON
├── load.py          # Stage 3: Inserts cleaned data into PostgreSQL
│
├── .env             # Secret credentials (API URL, DB password) — NOT committed to Git
├── .gitignore       # Excludes .env, venv/, __pycache__/ from version control
│
├── venv/            # Python virtual environment (excluded from Git)
└── README.md        # Project documentation (this file)
```

---

## ⚙️ How It Works — Pipeline Flow

```
main.py
   │
   ├── 1. fetch_data()          ← extract.py
   │       │
   │       └── Calls Open-Meteo API URL (from .env)
   │           Returns raw JSON response
   │
   ├── 2. transform_weather_data()   ← transform.py
   │       │
   │       └── Extracts: temperature, windspeed, timestamp
   │           Returns a clean Python dictionary
   │
   └── 3. weather_data()        ← load.py
           │
           └── Connects to PostgreSQL
               Inserts the record into `weather_data` table
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **requests** | Makes HTTP GET requests to the weather API |
| **python-dotenv** | Loads secrets from the `.env` file |
| **psycopg2** | PostgreSQL database adapter for Python |
| **PostgreSQL** | Database to store the weather records |
| **Open-Meteo API** | Free, public weather data API (no API key required) |

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have the following installed:
- Python 3.8+
- PostgreSQL (running locally on port `5432`)
- `pip` (Python package manager)

---

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd Basic_ETL_Weather
```

---

### 3. Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install requests python-dotenv psycopg2-binary
```

---

### 5. Configure the `.env` File

Create a `.env` file in the project root (or edit the existing one):

```env
DB_PASSWORD = "your_postgres_password"
API_KEY = "https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&current_weather=true"
```

> ⚠️ **Never commit your `.env` file to Git.** It is already listed in `.gitignore`.

---

### 6. Set Up the PostgreSQL Database

Open **pgAdmin** or **psql** and run the following SQL to create the database and table:

```sql
-- Create the database
CREATE DATABASE weather_db;

-- Connect to the database
\c weather_db

-- Create the table
CREATE TABLE weather_data (
    id          SERIAL PRIMARY KEY,
    city        VARCHAR(100),
    temperature FLOAT,
    windspeed   FLOAT,
    recorded_at VARCHAR(50)
);
```

---

### 7. Run the Pipeline

```bash
python main.py
```

**Expected Output:**
```
ETL Pipeline Running......
Connecting with weather API...
Data fetched!!
data transform Successfully!!
Data Successfully Loaded into the Database..
--- Pipeline Finish Successfully!! ---
```

---

## 📄 File-by-File Breakdown

### `main.py` — Pipeline Orchestrator
The entry point of the project. It imports and calls all three ETL stages in sequence. If any stage fails, the pipeline stops gracefully with an error message.

```python
run_pipeline()
  ├── fetch_data()            # Extract
  ├── transform_weather_data() # Transform
  └── weather_data()          # Load
```

---

### `extract.py` — Data Extraction
- Loads the `.env` file using `load_dotenv()`
- Reads the API URL from the `API_KEY` environment variable using `os.getenv()`
- Makes an HTTP GET request to the Open-Meteo API using `requests`
- Returns the raw JSON response on success, or `None` on failure

**API used:** [Open-Meteo](https://open-meteo.com/) — Free, no API key required (the full URL is stored in `.env`)

---

### `transform.py` — Data Transformation
- Receives the raw JSON dictionary from `extract.py`
- Extracts the `current_weather` block
- Returns a clean, flat dictionary with only 3 fields:

```python
{
    "temperature": 29.5,   # °C
    "windspeed": 11.2,     # km/h
    "timestamp": "2023-10-27T12:00"
}
```

---

### `load.py` — Data Loading
- Connects to the local PostgreSQL database (`weather_db`) using `psycopg2`
- Reads the database password securely from the `.env` file
- Inserts the cleaned weather record (hardcoded city: **Mumbai**) into the `weather_data` table
- Commits the transaction and closes the connection safely
- Handles any database errors with a `try/except` block

---

### `.env` — Environment Variables
Stores sensitive configuration that should **never** be hardcoded:

| Variable | Description |
|----------|-------------|
| `DB_PASSWORD` | PostgreSQL database password |
| `API_KEY` | Full Open-Meteo API URL with coordinates |

---

### `.gitignore` — Git Exclusions
Prevents the following from being committed to version control:
- `.env` — Credentials
- `venv/` — Virtual environment
- `__pycache__/` — Python bytecode cache
- `*.pyc` — Compiled Python files
- `.vscode/` — Editor settings

---

## 🗃️ Database Schema

**Database:** `weather_db`  
**Table:** `weather_data`

| Column | Type | Description |
|--------|------|-------------|
| `id` | `SERIAL PRIMARY KEY` | Auto-incremented unique ID |
| `city` | `VARCHAR(100)` | City name (currently: Mumbai) |
| `temperature` | `FLOAT` | Temperature in °C |
| `windspeed` | `FLOAT` | Wind speed in km/h |
| `recorded_at` | `VARCHAR(50)` | Timestamp from the API response |

---

## 🔧 Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError: name 'os' is not defined` | `import os` missing | Add `import os` at the top of the file |
| `os.getenv("API_KEY")` returns `None` | `.env` not loaded or key missing | Call `load_dotenv()` before `os.getenv()` |
| `psycopg2.OperationalError` | PostgreSQL not running or wrong credentials | Start PostgreSQL service; check `.env` password |
| `relation "weather_data" does not exist` | Table not created | Run the SQL setup script from Step 6 |
| `Failed to fetch the data: 4xx/5xx` | Bad API URL | Check the `API_KEY` URL in `.env` |

---

## 🔮 Possible Future Improvements

- [ ] Add a `requirements.txt` for easy dependency installation
- [ ] Schedule the pipeline to run automatically (e.g., using `cron` or `Windows Task Scheduler`)
- [ ] Support multiple cities dynamically
- [ ] Add logging (using Python's `logging` module) instead of `print` statements
- [ ] Store `recorded_at` as a proper `TIMESTAMP` column in PostgreSQL
- [ ] Add a data visualization dashboard (e.g., Grafana or Streamlit)
- [ ] Write unit tests for each ETL stage

---

## 👤 Author

**Harshil**  
Data Engineering Project — Basic ETL Pipeline  
Built with Python & PostgreSQL

---

## 📜 License

This project is open-source and available for learning and experimentation.