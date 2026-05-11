x={1,2,3,4}
print(type(x))
print(x)

#2 way --set([__])
y=set([1,2,3])
print(type(y))
print(y)

#methods
#1ADD
a={1,2}
a.add(3)
print(a)

#2UPDATE
a.update([4,5,6])
print(a)

#REMOVE
a.remove(5)
print(a)

#DISCARD
a.discard(6)
print(a)
a.discard(16)
print(a)

#POP()-Random
a.pop()
print(a)

#clear--empty
a.clear()
print(a)

#operatiional 
#1 union
a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)

print(a.symmetric_difference(b))
print(a^b)

#checking methods
#1.SUBSET
a={1,2}
b={1,2,3}
print(a.issubset(b))
print(b.issubset(a))

#2.SUPERSET
print(a.issuperset(b))
print(b.issuperset(a))

#DISJOINT
x={1,2}
y={3,4}
z={1,2}
print(x.isdisjoint(y))
print(x.isdisjoint(z))

#functions
x={23,4,5,34,6}
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x))

#----------------------------
java_student={"ram","rahul","komal"}
python_student={"rahul","sakshi","radha"}

#total student count
total_student=java_student.union(python_student)
print("Total students:",total_student)
for name in total_student:
    print(name)
print(len(total_student))

#common student
common_student=java_student.intersection(python_student)
print("Common student:",common_student)
for name in common_student:
    print(name)
print(len(common_student))

#unique
print(java_student.difference(python_student))
print(python_student.difference(java_student))



