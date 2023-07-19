# program 1
# list example
# it store the value by index

fruits=["apple","mango","banana","papaya","pineapple"]
print(type(fruits))

# dictionary(like object)
# it doesn't store the value by index
# program 1
info={
    "firstName":"Kalyani",
    "lastName":"Hadole",
    "age":23,
    "rollNo":12
}

print(info)
print(type(info))

# program 2

bank={
    "accNumber":12343221,
    "holderName":"Kalyani",
    "bankName":"sbi",
    "Branch":"Vaijapur",
    
}

# retrive
print(bank["accNumber"])

# add
bank["pincode"] = 324356
print(bank)

# udpate
bank['accNumber'] = 456
print(bank)

# del
del bank['bankName']
print(bank)

# program 3

MH = {
    "city1":"pune",
    "city2":"mumbai"
}
print(MH['city1'])
print(MH['city2'])

# add the property to dict
MH['city3'] = "Gujrat"
print(MH)

# update
MH['city2'] = "Rajasthan"
print(MH)

del MH['city3']
print(MH)

# program 4

vehicle = {
    "color":"Black",
    "type":"BMW",
    "modelNo":1234
}

# retrive

print(vehicle['color'])

# add

vehicle['city']='PUNE'
print(vehicle)

# update
vehicle['modelNo']=6575
print(vehicle)

# ddelete
del vehicle['city']
print(vehicle)

