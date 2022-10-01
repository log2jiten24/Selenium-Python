import requests



resp = requests.get("https://www.google.com")
print('Status code', resp)

print('cookies details', resp.cookies)
print('status code', resp.status_code)
print('url ', resp.url)
print('text url', resp.text)


