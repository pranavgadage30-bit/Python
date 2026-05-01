rollno=[101,102,103]
#access:varname[indexno]
print(rollno[0])

#update
rollno[2]=107
print(rollno)

#student name
student_name=['abc','xyz','pqr','mno']
print(student_name)
print(student_name[1])
print(student_name[-1])

#mixed
mixed=[1,90.99,'ram','2.89.87','shyam']
print(mixed)
print(mixed[2])
print(mixed[-2])

#we can change the string value
mixed[2]='ramesh'
print(mixed)
print(type(mixed))

#list loop
for i in mixed:
    print(i)
    

#-----------------------------
x=[10,20,30,40,50]
print(10 in x)
print(90 in x)

#inbuilt
#add 1.append-last index  2.insert-(index no,value)
x.append(60)
print(x)
x.insert(2,100)
print(x)

#remove 1.remove(element) 2.pop(index)
x.remove(20)
print(x)
x.pop(4)
print(x)

#homework
a=[24,56,78,97,30]
#1.Even print
for i in a:
    if i%2==0:
      print (i)
      
#2.odd element sum
sum=0
for i in a:
    if i%2!=0:
        sum=sum+i
        print(sum)
        
#3.%5->square->cube
square=0
for i in a:
    if i%5==0:
       square=i**2
print(square**3)
        
#4.Reverse
print(a[::-1])

#5.even->0 odd->1
result=[]
for i in a:
    if i%2==0:
        result.append(0)
    else:
        result.append(1)
print(result)
        