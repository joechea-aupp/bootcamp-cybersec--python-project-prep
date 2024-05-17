# run the following command to install requests library
# pip install requests
import requests

url = 'https://icanhazdadjoke.com'
response = requests.get(url, headers={'Accept': 'application/json'})
print(response.text)
print(response.json()['joke'])


# get public ip address
public_ip_url = "http://ip.jsontest.com"
res = requests.get(public_ip_url, headers={'Accept': 'application/json'})
print(res.json())
