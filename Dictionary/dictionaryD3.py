# program 1

info={
    "firstName":"Kalyani",
    "lastName":"Hadole",
    "age":23,
    "city":"Pune"
}

print(info)
print(type(info))

info1=info
info1["firstName"]="Nilesh"
print(info)
print(info1)

# program 2


vehicle={
    "color":"Black",
    "modelNumber":234221,
    "type":"scorpio",
    "city":"Nagpur"
}

print(vehicle)

#copy
vehicle1=vehicle.copy()
vehicle1["color"]="purple"
print(vehicle)
print(vehicle1)

# get for get the specific keys
a=vehicle1.get('type')
print(a)    # Scorpio

# program 3

vehicle2 = {
        "color":"red",
        "type":"sedane",
        "regno":123
}

# pop
vehicle2.pop('type')
print(vehicle2)

# program 4

info3={
    "firstName":"Aryan",
    "lastName":"Pawar",
    "age":12,
    "city":"Nashik"
}

for a in info3:
    print(a,[info3])
# for print keys
for pro in info3.keys():
    print(pro)
# for print values
for val in info3.values():
    print(val)
# print both keys and values
for valkey in info3.items():
    print(valkey)
# clear
"""info3.clear()
print(info3) """ # {}

# fromKeyes
A1={"Dhanvi","Bangal","Nagpur"}
A2=None
q1=dict.fromkeys(A1,A2)
print(q1)


# program 5

info4 = {
        "language":"hindi",
        "city":"pune",
        "country":"India"
}

info4.popitem() # remove the last prop and values
print(info4)
q2 = info4.setdefault("language",None)
print(q2)








































vehicle1["type"]="sedane"
print(vehicle)
print(vehicle1)





















