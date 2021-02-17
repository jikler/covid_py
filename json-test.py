import json
from pprint import pprint

data = {}
data['users'] = []
data['users'].append({
    'name': 'Петрова Ирина2',
    'id': '1111111',
    'birthday': '24.12.1933',
    'sex': 'Женский'
})

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=1, ensure_ascii=False)

with open('data.json', 'r', encoding='utf-8') as outfile:
    text = json.load(outfile)
    pprint(text)
 
# with open('data.json', 'r', encoding='utf-8') as f:
#     text = json.load(f)
#     pprint(text)
