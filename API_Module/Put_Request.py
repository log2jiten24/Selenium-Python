# hitting the put request with data from the json file

import  requests
import  json

payload = {
    "name": "morpheus",
    "job": "zion resident"
}
#to know the data type of the payload
print(type(payload))
#pass the post method in the
response = requests.put("https://reqres.in/api/users/2",data=payload)

print(response.status_code)
#to get the response in json
print(response.json())

#add an assert verification for the response -
assert response.json()['job'] == 'zion resident'