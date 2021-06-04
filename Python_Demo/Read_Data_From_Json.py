import json


with open('order.json','r') as json_file:
    json_object = json.load(json_file)


print(len(json_object["orders"]))
print(json_object["orders"],[0],["toppings"])

print(json.dumps(json_object))

print(json.dumps(json_object,indent=1))