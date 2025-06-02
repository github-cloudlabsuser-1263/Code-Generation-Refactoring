# Fetch weather data from OpenWeatherMap API
import requests

API_KEY = "your_existing_openweathermap_api_key"
def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# Display weather information
def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.capitalize()}")
    else:
        print("Weather data not available.")

# Main function to run the weather script
def main():
    api_key = "6de8b9d8ab904eb2a6b15ef851bebdac"
    city = input("Enter the city name: ")
    
    weather_data = fetch_weather(api_key, city)
    display_weather(weather_data)
    