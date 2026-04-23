import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        data = response.json()
        print(f"Post Title: {data['title']}")
    else:
        print(f"Failed to hit API! Status: {response.status_code}")

except Exception as e:
    print(f"Network error occurred: {e}")
