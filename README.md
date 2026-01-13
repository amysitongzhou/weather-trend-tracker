# Weather Trend Tracker

A small personal project to track and analyze daily weather data using Python.
Tracks daily weather for Toronto, Waterloo, New York, Beijing, and Guangzhou, stores history, and analyzes long-term trends using Python

## Features

- Collects daily weather data (max/min temperature, precipitation) for multiple cities using the [Open-Meteo](https://open-meteo.com/) public API (no API key required).
- Stores data in a CSV file (`weather_data.csv`) to build a historical dataset over time.
- Provides basic analysis of weather history using Pandas (summary stats, trends).
- Visualizes temperature trends and rolling averages with Matplotlib charts.

## Files

- `collector.py` – Fetches today's weather for configured cities and appends it to `weather_data.csv`.
- `analyze.py` – Loads the CSV, prints basic statistics, and shows trend charts.
- `requirements.txt` – Python dependencies.

## How to run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

---

# 🚀 Final step — push to GitHub

From your project folder:

```bash
git init
git add .
git commit -m "Initial project: weather trend tracker"
git branch -M main
git remote add origin https://github.com/amysitongzhou/weather-trend-tracker.git
git push -u origin main
