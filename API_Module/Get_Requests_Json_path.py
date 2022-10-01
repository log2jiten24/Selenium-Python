#verification of json path - to get the particular element from the response :-
import requests

p = {"page" : 2}

resp = requests.get("https://reqres.in/api/users?" ,params= p)
print('Final URL value' , resp.url)
#get the value in the json format
json_resp = resp.json()

print(json_resp)

#to get the total value from the JSON Response payload
print(json_resp['total'])

assert json_resp['total'] == 12 , 'Total value in the JSON Payload not matching'

#to get the JSon response from the data array
print(json_resp['data'])
#get the 2nd element inside the json array
print(json_resp['data'][1])
#get the 2nd element inside the json array- value of email
print(json_resp['data'][1]['email'])

#get the last value from the response
print(json_resp['support']['url'])

