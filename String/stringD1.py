# program 1

firstName = "Kalyani"
print(type(firstName))

lastName = 'Hadole'
print(lastName)

# STRING
# String stores the value by index
city = "pune"

# 0    1   2   3
# p    u   n   e
print(city[0])
print(city[3])

city = "mumbai"
g = len(city)
print(g)
print(type(g))


#method
# program 2
#Uppar --String
city3 = "Nagpur"
q1  = city3.upper()
print(q1)
print(type(q1))

#Lower --String
city4 = "Bhopal"
q2 = city4.lower()
print(q2)
print(type(q2))

#Count -- Integer
city5  = "chandrapur"
q3 = city5.count('a')
print(q3)
print(type(q3))

# Method chaining
#upper() , lower() , count()
q4 = city5.upper().lower().count('a')
print(q4)

# program 3
#StartsWith---Boolean
city5 = "jaipur"
q5 = city5.startswith("j")
q6 = city5.startswith("jai")
print(q5)
print(q6)

# program 4
#endWith---Boolean
city6 = "Udaipur"
q7 = city6.endswith('r')
q8 = city6.endswith('pur')
print(q7)
print(q8)