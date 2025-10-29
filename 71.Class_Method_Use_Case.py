#use Class Method as a alternative constructor
class Employee:
    
    def __init__(self,name,company):
        self.name=name
        self.company=company
        
    @classmethod
    def Changeformat(cls,new_company):
        name,company=new_company.split("-")
        return cls(name,company)
        
    def show(self):
        print(f'{self.name} and company {self.company}')
        
string="Hasib-Dell"
e1=Employee.Changeformat(string)
e1.show()
