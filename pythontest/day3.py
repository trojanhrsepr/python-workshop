print(list(range(-1,12)))

with open("data.txt","r") as f1, open("two.txt", "w+") as f2:
    for record in f1:
        f2.write(record.upper())
    print(f1.closed)
print(f1.closed)

import pickle

config = {
    "name": "appserver",
    "ip": "192.168.1.1",
    "os": "linux",
    "data": [1, 2, 3, 4]
}

f1 = open("config.pickle", "wb")
pickle.dump(config, f1)
f1.close()

f2 = open("config.pickle", "rb")
res = pickle.load(f2)
print(res)
f2.close()

import json

config1 = {
    "name": "appserver",
    "ip": "192.168.1.1",
    "os": "linux",
    "data": [2, 3, 3, 4]
}

f1 = open("config1.json", "w")
json.dump(config1, f1)
f1.close()

f2 = open("config1.json", "r")
res = json.load(f2)
print(res)
f2.close()


def function12(params):
    print(params)


function12(12)

# Differentiated between arguments based on type. Dictionary type mapped into **


def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(10, 20, 30, a=1, b=2)


def fun():
    print("I am a function object")


fun = "I am a string"
# 'str' object is not callable
# fun()
print(fun)










