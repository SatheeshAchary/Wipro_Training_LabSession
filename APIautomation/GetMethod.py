from xml.etree.ElementTree import indent

import requests
from requests.auth import HTTPBasicAuth

# make a get request to a api endpoint
try:

    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame", auth=HTTPBasicAuth('username', 'password'), timeout=5, headers=headers)
    print(response)

    if response.status_code == 200:
        print("Status code is 200 OK")
        data = response.json()
        print(data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")