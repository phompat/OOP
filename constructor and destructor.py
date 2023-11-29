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
        
    #create destructor(ไม่ระบุก็ได้)
    def __del__(self):
        print("call destructor")
 

#create object->เรียกใช้จริง
emp1=Employee("kong",50000,"accoutant")
emp1.salary = 56000
emp1.department = "singer"
emp1.showdata()

emp2=Employee("phurich",100000000,"rich man")
emp2.showdata()
