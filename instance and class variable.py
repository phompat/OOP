class Employee:

    #ClASS VARIABLE
    _minsalary=12000
    _maxsalary=50000
    _companyname="บริษัท xyz จำกัด"
    def __init__(self,n,s,d):
        #instance variable
        self._name = n 
        self._salary = s 
        self._department= d 
    
    #private method
    def _showdata(self): 
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self._salary))
        print("ตำแหน่ง = {}".format(self._department))
   
emp1=Employee("kong",50000,"accoutant")
emp1._showdata()
print("เงินเดือนต่ำสุด = "+str(Employee._minsalary))#print class variable without creating object
print(Employee._companyname) 