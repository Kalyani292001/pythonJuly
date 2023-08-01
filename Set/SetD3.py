#Program 1
names={"Kalyani","Amol","Nilesh","Aryan"}
print(names)

# add()
names.add("Dhanvi")
print(names)

# clear()
names.clear()
print(names)

# copy() (same)

setA={11,22,33,44}
setB=setA
setA.remove(22)
print(setA)
print(setB)

setC=setA.copy()
setA.remove(11)
print(setA)
print(setC)

# difference()
# differnce_update()

setD={11,22,33}
setE={11,22,44}

print(setD.difference(setE))
setD.difference_update(setE)
print(setD)

setF = {11,22,33}
setG = {11,22,44}
setF.difference_update(setG)
print(setF)

# discard()===> delete the specific element

setH={1,2,3,4,5,6}
setH.discard(4)
print(setH)

# intersection()===> gives same element

setJ={1,2,3,4}
setK={1,2,3,4,5}

#print(setJ.intersection(setK))
setJ.intersection(setK)
print(setJ)

# intersection_update()
setJ.intersection_update(setK)
print(setJ)

# isdisjoint()
setJ.isdisjoint(setK)
print(setJ)

#issubset(),issuperset()====>return Boolean
print(setJ.issubset(setK))
print(setJ.issuperset(setK))

#Pop()===> remove last element
setI = {11,22,33}

setI.pop()
print(setI)

# remove()
setI.remove(22)
print(setI)


#union
setQ = {11,22,33,44}
setL = {44,55,66}
setS = setQ.union(setL)
print(setS)

#update()
setQ.update({444,555})
print(setQ)
setQ.update([666,7777,88888])
print(setQ)


#symmetric difference()
a= {1,2,3}
b = {1,4,6}
print(a.symmetric_difference(b))

a.symmetric_difference_update(b)
print(a)