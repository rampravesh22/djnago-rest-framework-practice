import requests
import json
URL = "http://127.0.0.1:8000/student/"
# read data from database
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data(3)
#post data or create data into database
def post_data():
    data = {
        'name':12
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
    
# post_data()

#update data in database 
def update_data():
    data = {
        'id':7,
        'name':"maharaja chandrashekhar"
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
    
# update_data()
    
    
# delete data from database
def delete_data():
    data = {
        'id':3,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
    
delete_data()
