x=[1,2]
y=[3,4]
#add on x
x.extend(y)
print(x)

#list clear
a=[10,20,30,40]
print(a)
a.clear()
print(a)

x=[1,2]
y=[3,4]
#add on x
x.extend(y)
print(x)
print(x.index(2))

#reverse
x=[12,34,56,20]
x.reverse()
print(x)

#copy
a=[10,20]
b=a.copy()
print(b[0])

#sort
x=[90,70,50,30,100]
x.sort()
print(x)

x.sort(reverse=True)
print(x)

#counting
a=[11,22,33,11,44,11]
print(a.count(11))