class Employee:#create class-> structure

    #create constructor
    def __init__(self,n,s,d):
        
        self._name = n #protected attribute
        self.__salary = s #private arribute
        self.__department= d #private arribute -->not be able to change it 
    
    #private method
    def _showdata(self): #if __showdata()--> in line22 emp1.__showdata, there is no output
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))


#create object->เรียกใช้จริง
emp1=Employee("kong",50000,"accoutant")
emp1.__salary=1000000
emp1._name= "phom"
emp1.__department="seller"
emp1._showdata()
