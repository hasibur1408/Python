class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Show(self):
        print(f'Employee name is {self.name}')
        print(f'Employee salary is {self.salary}')
class Manager(employee):
    def __init__(self, name, salary,department):
        self.department=department
        super().__init__(name, salary)
    def Show(self):
        super().Show()
        print(f'Department is {self.department}\n')
class Programmer(employee):
    def __init__(self,name,salary,language):
        self.language=language
        super().__init__(name,salary)
    def Show(self):
        super().Show()
        print(f'Employee programming Language is {self.language}')
    
M=Manager("Hasibur",100000,"IT")
M.Show()
P=Programmer("Chad",20000,"Python")
P.Show()
    