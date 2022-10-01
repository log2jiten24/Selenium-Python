import requests

resp = requests.get("https://reqres.in/api/users?page=2")
print(resp)
#to check the type of response object
print(type(resp))

#to check the amount of methods available to check with the response object
#print(dir(resp))

#to assert the status code
code = resp.status_code
assert code == 200, 'Status code dont matches'

#get the response of the Data in String -unicode format - use the text method
#print(resp.text)
#get the response in the byte format
#print(resp.content)
#get the response in the JSON format
print(resp.json())

#now lets try to print all the headers
print(type(resp.headers))
print(resp.headers)

#now lets try to get the url - which we are hitting, encoding , cookies
print(resp.url)
print(resp.cookies)
print(resp.encoding)
