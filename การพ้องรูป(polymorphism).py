#overloading& overriding method

class Employee:
    __minsalary=12000
    __maxsalary=500000
    def __init__(self,n,s,d):
        self._name = n 
        self._salary = s 
        self._department=d
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self._salary))
        print("ตำแหน่ง = {}".format(self._department))
    def _getincome(self):
        return self._salary*12
    def _getincome(self,bonus=0,ot=0):#####overloading method
        return (self._salary*12)+bonus+ot
    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} ,เงินเดือน = {} ,รายได้ต่อปี = {}".format(self._name,self._department,self._salary,self._getincome()))



class Accounting(Employee):
    __departmentname="แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentname)
        self.__age=age
    def _showdata(self):#####overriding method
        super()._showdata()
        print("อายุ = {}".format(self.__age))
        print("*******")

    
class Programmer(Employee):
    __departmentname="นักพัฒนาระบบ"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentname)
        self.__exp=experience
        self.__skill=skill
    def _showdata(self):
        super()._showdata()
        print("ประสบการณ์ = "+self.__exp)
        print("skill = "+self.__skill)
        print("*******")


class Sale(Employee):
    __departmentname="ฝ่ายขายสินค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentname)
        self.__area=area
    def _showdata(self):#overriding method
        super()._showdata()
        print("พื้นที่ = "+self.__area)
        print("*******")
   

account= Accounting("Kong",12000,30)
programmer =Programmer("Jojo",40000,"1 year" ,"coding")
sale=Sale("Nut",35000,"chaing mai")
print("รายได้ตอ่ปีของนักบัญชี = {}".format(account._getincome()))
account._showdata()
print("รายได้ตอ่ปีของนักโปรแกรมเมอร์= {}".format(programmer._getincome(50000)))
programmer._showdata()
print("รายได้ตอ่ปีของนักขาย = {}".format(sale._getincome(300,1)))
sale._showdata()



