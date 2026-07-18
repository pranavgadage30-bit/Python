#STATIC METHOD
class demo:
    pass
    @staticmethod
    def welcome():
        print("Hello Static")
        
#1 way
demo.welcome()

#2 way 
obj=demo()
obj.welcome()

#---------------------------------------
class demo:
    pass
    name="Ram"
    @staticmethod
    def welcome():
        print(demo.name)
    
    @classmethod
    def xyz(cls):
        print(cls.name)
        print(demo.name)
        
demo.welcome()
demo.xyz()