import json

def readJsonData(filename,r):
    jsonfile=open(filename,r)
    jsondata= jsonfile.read()
    return (jsondata)

def writeJsonData(new_data,filename,w):
    jsonfile=open(filename, 'w')
    jsondata=json.dump(new_data, jsonfile, indent=4)
    return(jsondata)


def loadJsonData(jsondata):

    data = json.loads(jsondata)
    print(data)
    return (data)

def StoreDatainArray(data,details):
    list=data[details]
    print(list)
    return(list)




