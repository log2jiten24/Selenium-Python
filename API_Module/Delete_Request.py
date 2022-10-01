# hitting the Delete   request with data from the json file

import  requests


#pass the post method in the
response = requests.delete("https://reqres.in/api/users/2", timeout=5)

print(response.status_code)
#to get the response in json
assert response.status_code == 204