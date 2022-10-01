# hitting the post request with data from the json file

import  requests

import simplejson
import chardet
import simplejson
#open the json payload and read it
payload = open('json_payload.json', 'r').read()

#pass the post method  and deserialize - the String Object into the Python Dictionary Object
response =   requests.post("https://reqres.in/api/users",data= simplejson.loads(payload))
print(response.status_code)
#to get the response in json
print(response.json())
#add an assert verification for the response -
assert response.json()['job'] == 'leader', 'if not match Leader id failing '

#print the headers
print(response.headers.get("Content-type"))

