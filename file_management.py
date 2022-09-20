import json
"""
try:
    file = open("currency.json",'r')
except:
    file = open("F:\Python Training\data/currency.json",'w+')
"""
file = open('currency.json', 'w')
currency = [
    {
        "currency": "NPR",
        "exchange_rate": 125
    },
    {
        "currency": "INR",
        "exchange_rate": 78
    }
]
_json_str = json.dumps(currency, indent=4)
print("Json string: ", _json_str)

_json_dict = json.loads(_json_str)
print("Json Dict: ", _json_dict)

file.write(_json_str)

file.close()