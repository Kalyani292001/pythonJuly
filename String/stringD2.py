# Program 1

# STRIP()===> remove the first and last space
q1=" Kalyani "
print(q1.strip())
print(len(q1))

#program 2

#isDigit()====> Boolean (only integer)

q2="12343"
print(q2.isdigit())

q3="12343K"
print(q3.isdigit())

# program 3
#isAlpha()====>Boolean(only alphabet)

q4="kalyani"
print(q4.isalpha())

q5="kalyani29"
print(q5.isalpha())

# program 4
# isalnum()===>Boolean(only character aur interger allow/special character not allow)

q6="Kalyani29"
print(q6.isalnum())

q7="Kalyani@29"
print(q7.isalnum())

#program 5
# replace()===>String

q8="I am learning the Javascript"
print((q8.replace("Javascript","python")))

# program 6
#Split()===> string

q9="kalyaniihadole"
print(q9.split("i"))   #['kalyan', '', 'hadole']

# program 7
q10 = " jaipur "
print(len(q10))

q9 = q10.strip()
print(q9)
print(len(q9))

# program 8

info = "Kalyani Navnath Hadole"
q10 = info.split(" ")
print(q10)


# program 9
email = "kalyanihadole29@gmail.com"
q11 = email.split('@')
print(type(q11))
print(q11)


# program 10
info3 = "I am learning javaScript"
q12 = info3.replace("javascript","python")
print(q12)

# program 11
'''mks = "11"
q13 = mks.id()
print(q13)'''


# program 12
mks2 = "adasdsa"
q14 = mks2.isalpha()
print(q14)

# program 13
mk3 = "A213213 "
q15 = mk3.isalnum()
print(q15)

#program 14

city7 = " goa "
# print(len(city7))
# q1 = city7.strip()
# print(len(q1))

# program 15
city8 = " Bhopal"
q2 = city8.lstrip()
print(len(q2))

# program 16
city9 = " wardha "
print(len(city9))
q3 = city9.rstrip()
print(len(q3))

# program 17
info = "I am  learning js "
q4 = info.title()
print(q4)

# program 18
city10 = "Gujrat is nice place to leave"
q5 = city10.capitalize()
print(q5)

# program 21
city11 = "NaGpur"
q6 = city11.swapcase()
print(q6)

# program 22

city13 = "jaipur"

# 0     1    2    3    4   5
# j     a    i    p    u   r
q7 = city13.index("a")
print(q7)

# 0  1  2  3  4  5  6  7  8  9 10 11 12
# c  h  a  n  d  r  a  p  u  r  a  e  a

city14 = "chandrapuraea"
q8 = city14.index("a",5)
print(q8)

q9 = city14.index("a",7,11)
print(q9)

first_name = "Kalyani"
lastName = "Hadole"
print("My firstname is {} and lastName is {}".format(first_name,lastName))


# ----------------------------------------------------------------
# 'in' keyword

fruits = "apple mango banana chikoo papaya"
if "apple" in fruits:
    print("fruit is available")
else:
    print("fruit is not available")


print("c" in "chinmay")