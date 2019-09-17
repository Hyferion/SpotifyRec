import requests
import json


def read_database():
    r = requests.get('https://spotifyrec-36551.firebaseio.com/.json')
    json_string = r.json()

    if json_string:
        with open("../Data/DatabaseExports/data.json", 'w', encoding='utf-8') as f:
            json.dump(json_string, f, ensure_ascii=False)
    print(json_string)
