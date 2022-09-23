import sys, json

data = json.loads(sys.argv[1])

text = data['text']

newData = {'result': text}

print(json.dumps(newData))