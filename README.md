# Weather Trend Tracker

This is a small Python project I built to collect and analyze daily weather data.
It tracks weather for cities like Toronto, Waterloo, New York, Beijing, and Guangzhou,
stores the data over time, and lets you explore basic temperature trends.

## What it does

- Pulls daily weather data (max/min temperature and precipitation) from the Open-Meteo API  
  (no API key needed)
- Saves each day’s data to a CSV file so a history builds up over time
- Uses Pandas to calculate basic statistics and trends
- Creates simple visualizations and rolling averages with Matplotlib

## Project structure

- `collector.py` – Fetches daily weather data for each city and appends it to `weather_data.csv`
- `analyze.py` – Loads the data and generates statistics and plots
- `requirements.txt` – Lists required Python libraries

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
python collector.py
python analyze.py
