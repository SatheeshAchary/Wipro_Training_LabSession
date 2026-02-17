import requests
import json


# Fetch all users and print usernames in uppercase
def fetch_users_uppercase():
    print("\nFetch users and print usernames in uppercase")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()

        users = response.json()
        for user in users:
            print(user["username"].upper())

    except requests.exceptions.RequestException as e:
        print("Error:", e)


#Implement timeout handling (2 seconds)
def timeout_handling():
    print("\nTimeout Handling (2 seconds)")
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
            timeout=2
        )
        print("Request successful:", response.status_code)

    except requests.exceptions.Timeout:
        print("Request timed out!")

    except requests.exceptions.RequestException as e:
        print("Other error:", e)


#Use Session object & demonstrate cookie persistence
def session_example():
    print("\nSession Example (Cookie Persistence)")

    session = requests.Session()

    # Set cookie
    session.get("https://httpbin.org/cookies/set/sessionid/12345")

    # Retrieve cookies
    response = session.get("https://httpbin.org/cookies")

    print("Cookies stored in session:")
    print(response.json())


# Upload a file using requests
def upload_file():
    print("\nUpload File Example")

    try:
        with open("test.txt", "w") as f:
            f.write("This is a test file.")

        with open("test.txt", "rb") as file:
            files = {"file": file}
            response = requests.post("https://httpbin.org/post", files=files)

        print("Upload response:")
        print(response.json())

    except Exception as e:
        print("File upload error:", e)


#Fetch posts and save into posts.json
def save_posts_to_file():
    print("\nFetch posts and save to posts.json")

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()

        posts = response.json()

        with open("posts.json", "w") as file:
            json.dump(posts, file, indent=4)

        print("posts.json file created successfully!")

    except requests.exceptions.RequestException as e:
        print("Error fetching posts:", e)


# Main execution
if __name__ == "__main__":
    fetch_users_uppercase()
    timeout_handling()
    session_example()
    upload_file()
    save_posts_to_file()
