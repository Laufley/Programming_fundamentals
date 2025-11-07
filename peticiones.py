import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200 :
    print("Respuesta correcta")
    print(response.json())
    print(response.json()["email"])
    print(response.json()["company"]["name"])
else :
    print(f"Error: {response.status_code}")