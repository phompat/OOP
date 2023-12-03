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
        print("แผนก = {}".format(self._department))

#classสืบทอดemployee
class Accounting(Employee):
    __departmentname="แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)

class Programmer(Employee):
    __departmentname="นักพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)#ส่งไปใช้งานที่constructor classแม่


class Sale(Employee):
    __departmentname="ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)
   
#object
account= Accounting("Kong",12000)
account._showdata()
programmer =Programmer("Jojo",40000)
programmer._showdata()
sale=Sale("Nut",35000)
sale._showdata()



##print(account._Employee__minsalary)#เมื่อminsalaryเป็นprivate


