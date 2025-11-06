class Animal:
    def __init__(self,name,specis):
        self.name=name
        self.specis=specis
    def show(self):
        print(f"Animal name is {self.name} and specis is {self.specis}")
class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name,specis="Persian")
        self.color=color
    def show(self):
        print(f"Cat name is {self.name}, Specis is {self.specis} and color is {self.color}")
child=Cat("Jalauddi","Red")
child.show()
parent=Animal("Shahabuddi","Bengal")
parent.show()