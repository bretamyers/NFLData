
import requests
import json

#data = json.load()

#jsonFile = open("/Users/BretMac/Downloads/2010082051.json")
#data = json.load(jsonFile)
#print(data)

class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None

        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)

            if not val:
                break;

        return val

with open("/Users/BretMac/Downloads/2010082051.json") as jsonFile:
    data = json.load(jsonFile)
    #print(data)

    #for key, value in data.items():
    #    print(str(key) + " value: " + str(data[key]))

    stack = data.items()
    while stack:
        k, v = stack.pop()
        if isinstance(v, dict):
            stack.extend(v.IterItems())
        else:
            print("%s: %s" % (k, v))
