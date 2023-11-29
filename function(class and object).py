class Employee:#create class-> structure

    #create constructor
    def __init__(self,n,s,d):
        self.name = n
        self.salary = s
        self.department= d
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))


#create object->เรียกใช้จริง
emp1=Employee("kong",50000,"accoutant")
emp2=Employee("phurich",100000000,"rich man")

#check whether it is a part of class Employee or not
print(isinstance(emp1,Employee))

#checkมีmethod , attribute อะไรบ้าง
print(dir(emp1))

#check emp สร้างจากclassอะไร
print(emp1.__class__)