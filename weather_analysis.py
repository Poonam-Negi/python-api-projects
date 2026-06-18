import requests
import pandas as pd

# url = "https://api.open-meteo.com/v1/forecast?latitude=28.6519&longitude=77.2315&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,relative_humidity_2m,wind_speed_10m&utm_source=chatgpt.com"

# Cities with latitude and longitude
cities = [
    ("Delhi", 28.6519, 77.2315),
    ("Mumbai", 19.0760, 72.8777),
    ("Ghaziabad", 28.6692, 77.4538),
    ("Shimla", 31.1048, 77.1734),
    ("Kolkata", 22.5726, 88.3639)
]

# Store weather data
weather_data = []

for city_name, lat, lon in cities:
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    response = requests.get(url)

 # Check if request was successful
    if response.status_code == 200:
       data = response.json()
       current = data["current"]
       temperature = current["temperature_2m"]
       humidity = current["relative_humidity_2m"]
       wind_speed = current["wind_speed_10m"]

       city_weather = {
            "City": city_name,
            "Temperature": temperature,
            "Humidity": humidity,
            "Wind Speed": wind_speed
        }
       weather_data.append(city_weather)

    else:
        print(f"Failed to fetch data for {city_name}")    

# Create DataFrame
df = pd.DataFrame(weather_data)

# Display DataFrame
print("\nWeather Data:")
print(df)

# Save to CSV
df.to_csv("weather_data.csv", index=False)

print("\nCSV file saved as weather_data.csv")

# Analysis

# Hottest City
hottest_city = df.loc[df["Temperature"].idxmax()]

# Average Temperature
average_temperature = df["Temperature"].mean()

# Highest Humidity
highest_humidity_city = df.loc[df["Humidity"].idxmax()]

print("\n===== Weather Analysis =====")

print(
    f"Hottest City: {hottest_city['City']} "
    f"({hottest_city['Temperature']} °C)"
)

print(
    f"Average Temperature: "
    f"{average_temperature:.2f} °C"
)

print(
    f"Highest Humidity: "
    f"{highest_humidity_city['City']} "
    f"({highest_humidity_city['Humidity']}%)"
)


