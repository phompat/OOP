class Employee:#create class-> structure

    # create method->actions 
    def details(self,n,s,d):
        self.name = n
        self.salary = s
        self.department= d

    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))
 


#create object->เรียกใช้จริง
emp1=Employee()
emp1.details("kong",50000,"accoutant")
emp1.showdata()

emp2=Employee()
emp2.details("phurich",100000000,"rich man")
emp2.showdata()
