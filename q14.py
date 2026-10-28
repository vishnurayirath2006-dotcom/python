
import json
import pandas as pd

# Sample weather data in JSON format
weather_json = """
[
    {
        "location": {
            "city": "Kochi",
            "country": "India"
        },
        "weather": {
            "temperature": 30,
            "humidity": 75
        }
    },
    {
        "location": {
            "city": "Delhi",
            "country": "India"
        },
        "weather": {
            "temperature": 35,
            "humidity": 40
        }
    },
    {
        "location": {
            "city": "Mumbai",
            "country": "India"
        },
        "weather": {
            "temperature": 32,
            "humidity": 65
        }
    },
    {
        "location": {
            "city": "Bengaluru",
            "country": "India"
        },
        "weather": {
            "temperature": 26,
            "humidity": 55
        }
    }
]
"""

# Parse JSON data
data = json.loads(weather_json)

# Extract weather details
records = []

for item in data:
    city = item["location"]["city"]
    country = item["location"]["country"]
    temperature = item["weather"]["temperature"]
    humidity = item["weather"]["humidity"]

    records.append({
        "City": city,
        "Country": country,
        "Temperature (C)": temperature,
        "Humidity (%)": humidity
    })

# Convert data into a table
df = pd.DataFrame(records)

print("WEATHER REPORT")
print(df.to_string(index=False))

# Generate summary
print("\nWEATHER SUMMARY")
print("Average temperature:",
      round(df["Temperature (C)"].mean(), 2), "C")

print("Average humidity:",
      round(df["Humidity (%)"].mean(), 2), "%")

# Find the city with the highest temperature
hottest = df.loc[df["Temperature (C)"].idxmax()]

print("Hottest city:", hottest["City"])
print("Highest temperature:",
      hottest["Temperature (C)"], "C")
