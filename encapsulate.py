class Employee:
    def __init__(self):
        self.name = "srinivas"
        self.__salary = 35000


class Details(Employee):
    def __init__(self):
        Employee.__init__(self)
        print("Calling private member of base class: ")
        print(self.__salary)


obj2 = Employee()
print(obj2.__salary)
obj1 = Details()
print(obj1.__salary)
