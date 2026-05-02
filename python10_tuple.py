t=(10,20,30,40)
#access
print(t[1])
print(t(-1))

#we cannot update tuple

t=(1,"ram",90)
print(t[1])
print(type(t))

#loop
for items in t:
    print(items)
    
#create tuple by providing single element
t=()
#t.append(10)no append function
print(t)

t=(100,200,50,78,34,200)
#inbuilt functions
print(len(t))
print(max(t))
print(min(t))
print(sorted(t))
print(sum(t))

#methods-->varname.methodname()
#count()/index
print(t.count(200))
print(t.index(78))
print(t.count(200,2))#indexing starts from 2nd inddex


x=[1,2,3]
print(x)
print(type(x))
y=tuple(x)
print(y)
print(type(y)) 

#membership operator-->in and not in
t=(56,67,98,23)
print(56 in t)
print(900 in t)

#programs
x=(45,65,34,78)
sum=0
for items in x:
    sum+=items
print(sum)

#even odd
evensum=0
oddsum=0
for items in x:
    if items%2==0:
        evensum+=items
    else:
        oddsum+=items
print(evensum,oddsum)

#minimum without loop
t=(10,20,5,30)
min=t[0]
for items in t:
    if items<min:
        min=items
print(min)

t=("ram",[10,20],90,70)
for items in t:
    if type(items)==list:
        for li_items in list:
            print(li_items)
    else:
        print(items)
    