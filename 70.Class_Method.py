class Employee:
    #Class Varable
    Company_Name="Apple"
    
    def __init__(self,name):
        self.name=name
    @classmethod
    def ChangeCompany(cls,new_company):
        cls.Company_Name=new_company
        
    def show(self):
        print(f'{self.name} and company {self.Company_Name}')
e1=Employee("Hasib")
e1.ChangeCompany("Tesla")
e1.show()
print(Employee.Company_Name)