import requests

user = input("Enter github username : ")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print("Sorry! Username not found!")
    exit(1)

details = resp.json()   # Treat response as json and convert it to dict
print("Name       : ", details['name'])
print("Company    : ", details['company'])
print("Followers  : ", details['followers'])
