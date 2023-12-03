class Employee:
    __minsalary=12000
    __maxsalary=500000
    def __init__(self,n,s,d):
        self._name = n 
        self._salary = s 
        self._department=d
    #รายได้ต่อปี
    def _getincome(self):
        return self._salary*12
    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} ,เงินเดือน = {} ,รายได้ต่อปี = {}".format(self._name,self._department,self._salary,self._getincome()))


#classสืบทอดemployee
class Accounting(Employee):
    __departmentname="แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)#ส่งไปใช้งานที่constructor classแม่

class Programmer(Employee):
    __departmentname="นักพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)

class Sale(Employee):
    __departmentname="ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)
   
#object
account= Accounting("Kong",12000)
programmer =Programmer("Jojo",40000)
sale=Sale("Nut",35000)
print(account.__str__())
print(programmer.__str__())
print(sale.__str__())
#print("income accounting= {}".format(account._getincome()))


