from django.conf import settings
from django.shortcuts import render
import json
import urllib.request
import urllib.parse  # For safe URL encoding


def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'].strip()  # Remove leading/trailing spaces from user input

        # Use your API key from settings
        api_key = "02f72abe0797438cb43fdc75924707fc"

        # Construct the API URL properly
        url = f'http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&appid={api_key}'

        try:
            # Fetch the response from the API
            response = urllib.request.urlopen(url).read()

            # Convert JSON response to a Python dictionary
            list_of_data = json.loads(response)

            # Prepare data for rendering
            data = { 
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                "temp": f"{list_of_data['main']['temp'] -  273.15:.2f}°C", 
                "pressure": str(list_of_data['main']['pressure']), 
                "humidity": str(list_of_data['main']['humidity']), 
                "description": list_of_data['weather'][0]['description'],  # Adding weather description
            } 
        except Exception as e:
            data = {"error": f"Could not retrieve data: {e}"}

    else: 
        data = {}  # Empty data for GET requests

    return render(request, "main/index.html", {"data": data})

