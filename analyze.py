"""
analyze.py

Loads weather_data.csv and performs basic analysis:
- summary statistics
- line charts for each city
- optional rolling average trends
"""

from typing import List

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "weather_data.csv"


def load_data() -> pd.DataFrame:
    """Load the weather data CSV into a DataFrame."""
    df = pd.read_csv(DATA_FILE)
    df["date"] = pd.to_datetime(df["date"])
    return df


def basic_stats(df: pd.DataFrame) -> None:
    """Print basic statistics for all numeric columns."""
    print("=== Overall statistics ===")
    print(df.describe())
    print()


def plot_city_temps(df: pd.DataFrame, city: str) -> None:
    """Plot daily max/min temperatures over time for a single city."""
    city_df = df[df["city"] == city].sort_values("date")

    if city_df.empty:
        print(f"No data for city: {city}")
        return

    plt.figure()
    plt.plot(city_df["date"], city_df["tmax"], label="Tmax (°C)")
    plt.plot(city_df["date"], city_df["tmin"], label="Tmin (°C)")
    plt.title(f"Daily Temperatures – {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_rolling_average(df: pd.DataFrame, city: str, window: int = 7) -> None:
    """Plot rolling average temperatures for a city."""
    city_df = df[df["city"] == city].sort_values("date").copy()

    if city_df.empty:
        print(f"No data for city: {city}")
        return

    city_df["tmax_roll"] = city_df["tmax"].rolling(window).mean()
    city_df["tmin_roll"] = city_df["tmin"].rolling(window).mean()

    plt.figure()
    plt.plot(city_df["date"], city_df["tmax_roll"], label=f"{window}-day Tmax avg")
    plt.plot(city_df["date"], city_df["tmin_roll"], label=f"{window}-day Tmin avg")
    plt.title(f"{window}-day Rolling Average Temperatures – {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()


def compare_periods(
    df: pd.DataFrame,
    city: str,
    date1_start: str,
    date1_end: str,
    date2_start: str,
    date2_end: str,
) -> None:
    """
    Compare average temperatures between two date ranges for a city.
    Dates should be strings like '2025-06-01'.
    """
    city_df = df[df["city"] == city]

    p1 = city_df[(city_df["date"] >= date1_start) & (city_df["date"] <= date1_end)]
    p2 = city_df[(city_df["date"] >= date2_start) & (city_df["date"] <= date2_end)]

    print(f"=== {city}: {date1_start} to {date1_end} vs {date2_start} to {date2_end} ===")
    print("Period 1 mean temps:")
    print(p1[["tmax", "tmin"]].mean())
    print("\nPeriod 2 mean temps:")
    print(p2[["tmax", "tmin"]].mean())
    print()


def main() -> None:
    df = load_data()
    basic_stats(df)

    # List of cities to analyze
    cities: List[str] = sorted(df["city"].unique())
    print("Cities in dataset:", ", ".join(cities))

    # Example: show charts for the first city (you can change this)
    if cities:
        example_city = cities[0]
        print(f"\nShowing charts for: {example_city}")
        plot_city_temps(df, example_city)
        plot_rolling_average(df, example_city, window=7)

    # Example of comparing two periods (adjust dates once you have enough data)
    # compare_periods(df, "Toronto", "2025-06-01", "2025-06-30", "2025-07-01", "2025-07-31")


if __name__ == "__main__":
    main()
