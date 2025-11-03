class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"my name is ('{self.name}') "
    def __repr__(self):
        return f"{self.name}'s age is {self.age}"
    def __call__(self, *args, **kwds):
        print("Hey this is callable function")
    def __len__(self):
        return len(self.name)
        

e=Employee("Hasib",21)

print(str(e))
print(repr(e))
print(len(e))
e()