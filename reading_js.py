import urllib.request as ur
import json

count_1 = int(0)
json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
count_1 += 1
for item in json_obj['comments']:
    sum += int(item['count'])
    count_1 += 1

print('Count:', count_1)
print('Sum:', sum)
