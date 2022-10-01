# hitting the post request with data from the json file

import  requests
import  json

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
#to know the data type of the payload
print(type(payload))
#pass the post method in the
response = requests.post("https://reqres.in/api/users",data=payload)

print(response.status_code)
#to get the response in json
print(response.json())

#add an assert verification for the response -
print(response.json()['id'])