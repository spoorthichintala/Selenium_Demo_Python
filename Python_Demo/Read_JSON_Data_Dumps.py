
# String with JSON format
import json


Client ={
{
	"name": "Jane Doe",
	"phone": "455-344-234",
	"email": "janedoe@email.com"

 }

}
# Convert JSON String to dictionary

client_Json=json.dumps(Client,indent=4,sort_keys=True)
print(client_Json)

