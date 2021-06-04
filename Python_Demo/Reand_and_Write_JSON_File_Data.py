import json

# function to add to JSON
def write_json(new_data, filename='TestData.json'):
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)

with open("TestData.json") as json_file:
    # First we load existing data into a dict.
    file_data = json.load(json_file)
    # Join new_dat3a with file_data
    temp = file_data["Login_details"]

    # python object to be appended
    y = {
        "uname": "Kumar",
        "upass": "Dixit"
    }
    temp.append(y)



write_json(y)
