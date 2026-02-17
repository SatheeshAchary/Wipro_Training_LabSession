import requests
import json


def basic_get():
    print("Fetch users - Name & Email")
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()

    for user in response.json():
        print(user["name"], "-", user["email"])


def get_with_param():
    print("\nPosts of userId=2")
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": 2}
    )
    response.raise_for_status()
    print("Number of posts:", len(response.json()))


def post_request():
    print("\nCreating a new post")
    payload = {
        "title": "Test",
        "body": "Testing API",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    if response.status_code == 201:
        print("Created Successfully")
    else:
        print("Failed")


def save_posts():
    print("\nSaving posts to file")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()

    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=4)

    print("Saved posts.json")

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception(f"API failed with status {response.status_code}")


if __name__ == "__main__":
    basic_get()
    get_with_param()
    post_request()
    save_posts()
