"""
collector.py

Collects daily weather data for configured cities and saves it into weather_data.csv.
Uses the Open-Meteo public API (no API key required).
"""

import csv
import os
from datetime import datetime
import requests

# === Your cities ===
CITIES = {
    "Toronto": {"lat": 43.65107, "lon": -79.347015},
    "Waterloo": {"lat": 43.4643, "lon": -80.5204},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Beijing": {"lat": 39.9042, "lon": 116.4074},
    "Guangzhou": {"lat": 23.1291, "lon": 113.2644},
}

OUTPUT_FILE = "weather_data.csv"


def fetch_daily_weather(city_name: str, lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "America/Toronto",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    daily = data["daily"]
    return {
        "date": daily["time"][0],
        "city": city_name,
        "tmax": daily["temperature_2m_max"][0],
        "tmin": daily["temperature_2m_min"][0],
        "precip": daily["precipitation_sum"][0],
    }


def ensure_csv_header(filename: str) -> None:
    header = ["date", "city", "tmax", "tmin", "precip"]
    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(header)


def append_weather_row(filename: str, row: dict) -> None:
    with open(filename, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(
            [row["date"], row["city"], row["tmax"], row["tmin"], row["precip"]]
        )


def main() -> None:
    print(f"[{datetime.now().isoformat(timespec='seconds')}] Collecting weather data...")
    ensure_csv_header(OUTPUT_FILE)

    for city, coords in CITIES.items():
        try:
            result = fetch_daily_weather(city, coords["lat"], coords["lon"])
            append_weather_row(OUTPUT_FILE, result)
            print(f"  Saved: {result}")
        except Exception as e:
            print(f"  Error collecting data for {city}: {e}")

    print("Done.")


if __name__ == "__main__":
    main()
