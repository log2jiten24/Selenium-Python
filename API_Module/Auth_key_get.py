import requests

#passing username and password as tuples
resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth= ('admin', 'admin'))

print(resp.status_code)