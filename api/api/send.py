import requests
import json

form={}
form["username"] = 'dmitry'
form["password"] = 'happyeaster'
#

t = requests.post('http://127.0.0.1:8000/api/token/', form)
js = t.json()
# print(js['refresh'])
# print(js['access'])


try:
    headers= {}
    headers["Authorization"] = 'Bearer '+ js['access']
    r = requests.get('http://127.0.0.1:8000/languages', headers=headers)
    # print(r.text)

    for i in r.json():
        print()
        for k,m in i.items():
            print(k,":",m)

    with open('api.json', 'w') as js_file:
        json.dump(r.json(), js_file)


except:
    print('bad token')
