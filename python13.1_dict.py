stud={
    "id":1,
    "name":"ram",
    "marks":90.89
}
print(stud)
print(type(stud))
#key-->values-->refvar["key"]
print(stud["name"])
print(stud["marks"])
print(stud.get("id"))

#update
stud["id"]=101
print(stud)

#loop
for key in stud:
    print(key)
    
for k,v in stud.items():
    print(k,v)

#methods
#1.return keys
print(stud.keys())
#2.values
print(stud.values())
#3.items
print(stud.items())
#pop
stud.pop("marks")
#copy
new_dict=stud.copy
print(new_dict)
#update()-->add/update
stud.update({"loc":"pune","div":"A"})
print(stud)
stud.update({"loc":"mumbai"})
#pop
stud.popitem()
print(stud)
#setdefault("key",value)
stud.setdefault("Passout year",2027)
print(stud)

#function:min,max,sorted,len
print(len(new_dict))
print(min(new_dict))
print(sorted(new_dict))

