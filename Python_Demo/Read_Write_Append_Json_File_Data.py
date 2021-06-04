import json

with open("TestData.json") as json_file:
    # First we load existing data into a dict.
    file_data = json.load(json_file)
    # Join new_data with file_data
    temp = file_data["Login_details"]
    # python object to be appended
    data = {
        "uname": "selenium",
        "upass": "Dixit"
    }
    temp.append(data)
# function to add to JSON
def write_json(new_data, filename='TestData.json'):
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)
def read_json(data):
    with open("TestData.json") as read_file:
        file_data1 = json.load(read_file)
        print(file_data1)
read_json(data)
write_json(data)