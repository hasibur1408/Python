class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
e=Employee("Hasib","21")
print(e.__dict__)
print(help(e))
print(dir(e))
        