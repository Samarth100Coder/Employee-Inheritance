class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)
class Employee(Person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,id)
a=Employee('Rahul',886012,200000,'Intern')
a.display()