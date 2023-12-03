class Employee:#create class-> structure

    #create constructor
    def __init__(self,n,s,d):
        
        self.__name = n 
        self.__salary = s 
        self.__department= d 
    
    #private method
    def _showdata(self): 
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.getsalary()))
        print("ตำแหน่ง = {}".format(self.__department))

    #setter method
    def setname(self,newname):
        self.__name= newname
    #
    def setsalary(self,newsalary):
        self.__salary=newsalary
    #
    def setdepartment(self,newdeparatment):
        self.__department=newdeparatment

    #getter method
    def getname(self):
        return self.__name
    #
    def getsalary(self):
        return self.__salary


#create object->เรียกใช้จริง
emp1=Employee("kong",50000,"accoutant")
emp1.setsalary(1000000)#if it is private attribute, you wanna change the salary
emp1.setname("Phom")
emp1.setdepartment("seller")
emp1._showdata()
print("พนังงานดีเด่น = ",format(emp1.getname()))#if it is private attribute,using getname is easier
print("เงินเดือน = ",format(emp1.getsalary()))