import pickle


class Employee():
    def __init__(self,eno,ename,marks):
        self.eno=eno
        self.ename=ename
        self.marks=marks

    def display(self):
        print("employee number is:", self.eno)
        print("employee name is:", self.ename)
        print("employee marks is:", self.marks)


with open("siva","wb") as f:
    e1 = Employee(101, "srinivass", 67)
    pickle.dump(e1,f)
    print("pickling of object is successfully")

with open("siva","rb") as f:
    obj=pickle.load(f)
    print("unpickling of object compleated")
    obj.display()
