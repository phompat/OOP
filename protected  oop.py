class Employee:

    def __init__(self,n,s,d):
        #protected attribut
        self._name = n
        self._salary = s
        self._department= d
    
    #protected method
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self._salary))
        print("ตำแหน่ง = {}".format(self._department))

emp1=Employee("kong",50000,"accoutant")
print(emp1._name)
emp1._salary=70000
emp1.name = "jojo"
emp1._name="phom"  # --> _คล้ายขอสิทธิแก้ข้อมูล
emp1._showdata()
