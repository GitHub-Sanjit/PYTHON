import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={
        "term":"cat"
    }
)

# print(f"your request to {url} came back w/ status code {response.status_code}")

data = response.json()
print(data['results'][1])
# print(type(response.text))
# print(type()) 

