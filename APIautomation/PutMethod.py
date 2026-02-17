import requests

from APIautomation.GetMethod import response

try:
    data = {
            "category": "Platform",
            "name": "Satheesh",
            "rating": "Mature",
            "releaseDate": "2012-05-04",
            "reviewScore": 85
        }

    response = requests.put("https://videogamedb.uk:443/api/v2/videogame/1", json = data)
    print(response)

    if response.status_code == 200:
        print("Status code is 200 OK")

        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
