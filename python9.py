x=[[1,2,3],[4,5,6],[7,8,9]]
#access sublist element
print(x[1])
#access particular element
print(x[2][1])

#access sublist
for i in x:
    print(i)

#access all particular elements of sublist    
for row in x:
    for col in row:
        print(col)
        
#update
x[1][5]=50
print(x)

student=[["amit",90],["ram",89],["sita",67]]
print(student)

#call every element
for row in student:
    for col in row:
        print(col)
        
#calling same index
#name:______ #marks:________
for row in student:
    print(f"name:{row[0]} marks:{row[1]}")
    
#update
student[2][0]="gita"
print(student)

#sum
sum=0
for marks in student:
    sum+=marks[1]
print[sum]

#display name who got greater marks than 89
for marks in student:
    if marks[1]>0:
        print("name",marks[0])
        
#displaying 0 for even marks and 1 for odd marks
for row in student:
    if marks[1]%2==0:
        row[1]=0
    else:
        row[1]=1
print(student)

#adding in list
student.append(["komal",100])

# Question 1
orders=[["pizza",1,200],["sandwich",2,400],["burger",4,1000],["fries",1,150]]

#total bill
sum=0
for i in orders:
    sum+=i[1]*i[2]
print("Total bill=",sum)

#gst bill
gst_bill=sum+sum*0.05
print("gst bill:",gst_bill)

#qty>3
for i in orders:
    if i[1]>3:
        print(i)
        
#10% hike
for i in orders:
    i[2]=i[2]+i[2]*0.10
print("New list:",orders)
    