import json

with open('3_numbers.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
    for i in range(len(new_dict)):
        print(new_dict[i])
