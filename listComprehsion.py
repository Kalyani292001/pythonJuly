# program 1

fruits = ["mango","banana","Kiwi","chikoo"]
newList = []

for item in fruits:
    newList.append(item)
print(newList)

# [expression for item in list if condition]
# program 2

q = [1,2,3,4,5,6,7,8,9,10]
sq = []
for item in q:
    sq.append(item*item)
print(sq)

q2 = [item * item for item in q]
print(q2)


# program 3
birthYear = [1988,1989,1990,1991]
q3=[2023 - item for item in birthYear]
print(q3)


# program 4
cities = ["pune","chennai","mumbai","kolkata"]
q4 =[item.upper() for item in cities]
print(q4)

#program 5

names = ["komal","aryan","kalyani","dhnavi","amol","nilesh"]
q5 = [item.upper() for item in names if len(item) >= 5]
print(q5)

# program 6
numbers = [11,22,44,55,22,33,44,55]
q6 = [item for item in numbers if item % 2 == 0]
print(q6)


# program 7
q7 = "books"
dictA = {}
for char in q7:
    dictA[char]= dictA.get(char,0) + 1
print(dictA)

# program 8
info  = {
    "firstName":"Kalyani",
    "lastName":"Hadole"
}

print(info['firstName'])
info.get('firstName')
info['age'] = info.get('age',22)
print(info)