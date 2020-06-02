import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    exit(1)

countries = resp.json()

for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    print(f"{country['name']:30} {country['population']:10}  {country['area']:15}")
