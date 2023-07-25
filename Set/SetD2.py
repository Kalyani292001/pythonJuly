# set
setA={"kalyani","nilesh","amol","aryan"}
print(setA)

# add
q1=setA.add("amruta")
print(q1)
print(setA)

# remove
setA.remove("kalyani")
print(setA)

# update
setA.update({"prasad","sai"})
print(setA)
# program 2

setB={"dhnavi","Bangal",11,32,"India"}
print(setB)
q2=setB.add("Pune")
print(setB)
print("Bangal" in setB)

if "India" in setB:
    print("element is present")
else:
    print("Element is not present")


# update
setC = {"pune" , "mumbai" ,"banglore" , "jaipur", "goa"}
print(setC)

setC.update({"wardha","chandrapur"})
print(setC)

setC.update(["nagpur","jabalpur"])
print(setC)

# program 3
setC2 = {'jabalpur', 'chandrapur', 'jaipur', 'nagpur', 'pune', 'banglore', 'mumbai', 'goa', 'wardha'}
setC2.remove('jaipur')
print(setC2)

# discard
setC2.discard("chandrapur")
print(setC2)

# pop
setC2.pop()
print(setC2)

#clear()
setC2.clear()
print(setC2)

# program 4
# union() (combine)
setA = {11,22,33}
setB = {33,44,55,66}
setC3 = setA.union(setB)
print(setC3)

# program 4

# intersection()
setD = {11,22,33}
setE  = {33,44,55,66}
setD = setE.intersection(setD)
print(setD)

# program 5

# issubset() issuperset()
setK = {1,2,3}
setS = {1,2}
print(setK.issubset(setK))
print(setS.issuperset(setS))

