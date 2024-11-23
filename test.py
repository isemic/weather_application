import urllib.request
import json

def get_weather_data(city):
    # Your API key
    api_key = "02f72abe0797438cb43fdc75924707fc"
    
    # Construct the API URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        # Send a request to the API
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())  # Parse JSON response

        # Extract desired information
        weather_data = {
            "city": city,
            "temperature": data['main']['temp'],
            "pressure": data['main']['pressure'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description'],
        }
        return weather_data

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Example usage:
city = "lahore"
weather_info = get_weather_data(city)
print(weather_info)
