import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "wiedzmin","likes": 10, "views": 10000}, {"name": "BMW Mechanic","likes": 67, "views": 10000}, {"name": "C++ tutorial","likes": 18910, "views": 10000},
        {"name": "how to sing","likes": 191919, "views": 10000}, {"name": "funny cows","likes": 110, "views": 10000}, {"name": "how to lift","likes": 515110, "views": 10000}]

for i in range(len(data)):
    response = requests.put(BASE + "Video/" + str(i), data[i])
    print(response.json())

response = requests.patch(BASE + "Video/1", {'views':1000})
print(response.json())

