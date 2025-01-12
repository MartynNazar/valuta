import requests


valcode = input("Введіть валюту:")
valdata = input("Введіть дату:")
response = requests.get(
    f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={valdata}&json")

data = response.json()

print(data)
print(data[0]["rate"])

