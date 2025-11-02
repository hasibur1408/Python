#parent Class
class Employee:
    def __init__(self,id,name,company):
        self.id=id
        self.name=name
        self.company=company
    def show(self):
        print(f"{self.id} {self.name} {self.company}",end=" ")
#Child Class      
class Programmer(Employee):
    def __init__(self,id,name,company,lang):
        super().__init__(id,name,company)
        self.lang=lang
        super().show()
        print(self.lang)


e1=Employee("101","Hasib","ClassiRaw")
e2=Programmer("102","Hasibur","Classi","Python")
        
        