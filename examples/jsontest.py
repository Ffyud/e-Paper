import json
import time

with open('../quotes.json') as jsonFile:
    quotes = json.load(jsonFile)

for i in quotes:
    quote = i['text']
    print(i['text'])
    time.sleep(5)