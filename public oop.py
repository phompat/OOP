class Employee:#create class-> structure

    #create constructor
    def __init__(self,n,s,d):
        #public attribut------> be able to change name ,salary , department 
        self.name = n
        self.salary = s
        self.department= d
    
    #public method
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))


#create object->เรียกใช้จริง
emp1=Employee("kong",50000,"accoutant")
emp1.salary=70000
emp1.name = "jojo"
emp1.showdata()
