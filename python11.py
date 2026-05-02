#NESTED TUPLE
x=(1,2,(3,4),(5,6),(7,(8,9)))
print(x[0])
print(x[2])
print(x[3][1])
print([4][1][1])

#concat
x=(1,2)
y=(3,4)
print(x+y)

#empty tuple
empty=()
name=input("Enter your name:")
id=int(input("Enter your id:"))
user=(name,id)
empty=empty+user
print(empty)