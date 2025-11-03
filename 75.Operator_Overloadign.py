# class Vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"
    
#     def __add__(self,other):
#         return Vector(self.i+other.i,self.j+other.j,self.k+other.k)
    
    
# v1=Vector(1,2,2)
# v2=Vector(2,3,4)
# print(v1+v2)

'''Equal Operator Overloading'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __eq__(self, value):
        return self.salary==value.salary
    
e1=Employee("Hasibur",1000)
e2=Employee("Chad",1000)
print(e1==e2)
    