# hitting the post request

import  requests

payload = {
    "name": "Jiten",
    "job": "leader"
}
#to know the data type of the payload
print(type(payload))
#pass the post method in the
response =   requests.post("https://reqres.in/api/users",data=payload)

print(response.status_code)
#to get the response in json
print(response.json())

#add an assert verification for the response -
assert response.json()['job'] == 'leader', 'Leader id failing '

