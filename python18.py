#OOPS
class demo:
    pass
    #class variable
    ins_name="Linkcode"
    
#1.class object
obj=demo()
print(obj.ins_name)

#2.class var -->classname.varname
print(demo.ins_name)

#---------------------------------------------
#VARIABLES-->1.Instance Variable 2.Class Variable
class stud:
    #instance variable
    def _init_(self):
        self.name=None
        self.age=0

#object
s1=stud()
#assign value-->refvar.instancevarname=value
s1.name="ram"
s1.age=90
print(s1.name,s1.age)

s2=stud()
s2.name="sita"
s2.age="85"
print(s2.name,s2.age)

#------------------------------------------------
#CONSTRUCTOR-->1.Default Constructor  2.Parametrized Constructor
class demo2:
    #default constructor
    pass
    def __init__(self):
        print("Default constructor is called")
    #parametrized constructor
    def __init__(self,name,age):
        self.sname=name
        self.sage=age
        
#obj=demo2()-->error
obj=demo2("Ram",90)
print(obj.sname,obj.sage)

obj2=demo2("Sita",85)
print(obj2.sname,obj2.sage)

#---------------------------------------------------------------
#METHODS-->CLASS METHOD
class demo():
    #class variable
    ins_name="linkcode"
    
    #class method
    @classmethod
    def update(cls):
        new_value=input("Enter new name:")
        cls.ins_name=new_value
        print("UPDATED!")
        
#1Way-->classname.methodname
demo.update()
print(f"Updated name is{demo.ins_name}")

#2Way-->objectrefvar.meth
obj=demo()
obj.update()
print(f"Updated name is{demo.ins_name}")

#-------------------------------------------------------------------
#INSTANCE METHOD
class demo:
    def __init__(self,name):
        self.name=name
        
    #instance method
    def update_name(self,new_name):
        self.name=new_name
        print(f"New name is {self.name}")
        
#demo.update_name("Ram")-->error:depends on object creation
#object
obj1=demo("Ram")
print(f"Current name is{obj1.name}")
obj1.update_name("Ramesh")

obj2=demo("sita")
print(f"Current name is{obj2.name}")
obj2.update_name("gita")
           

    