import json

first = 1
last = 75419

header_set = set()

for i in range(first, last + 1):
    try:
        json_data = json.load(open('../JSON/inmail.' + str(i) + '.json'))
        if 'headers' in json_data:
            for header in json_data['headers']:
                if header[0:2] == 'x-':
                    header_set.add(header)
    except:
        pass

print(header_set)
