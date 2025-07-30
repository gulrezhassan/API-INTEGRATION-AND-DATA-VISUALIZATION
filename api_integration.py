import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = "94ac565745015350117cb6eec251b8c9"
CITY = "London"
UNITS = "metric"  # Use 'imperial' for Fahrenheit

# API Endpoint
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

# Fetch data from OpenWeatherMap
response = requests.get(url)
data = response.json()

# Parse forecast data
dates = []
temps = []
weather_conditions = []

for entry in data["list"]:
    dt = datetime.fromtimestamp(entry["dt"])
    temp = entry["main"]["temp"]
    condition = entry["weather"][0]["main"]

    dates.append(dt)
    temps.append(temp)
    weather_conditions.append(condition)

# Plot 1: Temperature over time
plt.figure(figsize=(12, 5))
sns.lineplot(x=dates, y=temps, marker="o", color="orange")
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# Plot 2: Frequency of weather conditions
plt.figure(figsize=(8, 5))
sns.countplot(y=weather_conditions, palette="coolwarm", order=list(set(weather_conditions)))
plt.title(f"Weather Condition Frequencies in {CITY} (Next 6 Days)")
plt.xlabel("Frequency")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.show()
