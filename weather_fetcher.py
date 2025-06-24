import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        print(f"\nWeather in {city}:")
        print(f"Temperature: {main.get('temp', 'N/A')}°C")
        print(f"Feels like: {main.get('feels_like', 'N/A')}°C")
        print(f"Condition: {weather.get('description', 'N/A').title()}")
    else:
        print("\n[Error] Could not fetch weather data. Please check the city name or your API key.")

if __name__ == "__main__":
    print("=== Weather Fetcher (OpenWeatherMap) ===")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city = input("Enter city name: ").strip()
    get_weather(city, api_key)
