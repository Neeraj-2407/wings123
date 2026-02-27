#changing from json to python
import json

x = '{ "name":"neeraj", "age":22, "city":"mbnr"}'

y = json.loads(x)

print(y["age"])

#changing from python to json
import json

x = {
  "name": "neeraj",
  "age": 22,
  "city": "mbnr"
}

y = json.dumps(x)
print(y)
