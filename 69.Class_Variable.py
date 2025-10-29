class Employee:
    company_Name="Apple"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"{self.name} is {self.age} years old and he is working in {self.company_Name}")
        
e1=Employee("Hasib",27)
e1.show()
e2=Employee("Haibur",28)
Employee.company_Name="Dell"
e2.show()
e3=Employee("H",5)
e3.show()
print(Employee.company_Name)