import requests
# make a get request to a api endpoint
try:
    response = requests.delete("https://videogamedb.uk:443/api/v2/videogame/1")
    print(response)

    if response.status_code == 200:
        print("Status code is 200 OK")
        data = response.json()
        print(data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")