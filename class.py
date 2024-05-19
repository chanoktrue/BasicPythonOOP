
# Inheritance
class Employee:
    # class variable
    minSalary = 10000
    maxSalary = 30000
    companyName = "Company XYZ"
    
    def __init__(self, name, salary, department):
        # instance variable
        self.name = name
        self.__salary = salary
        self.__department = department
        
    def showData(self):
        print("\nstaff name = ", self.name)
        print("salary = ", format(self.__salary))
        print("department : {}".format(self.__department))
        
    def _getIncom(self, bonus = 0):
        return (self.__salary * 12) + bonus
    
    def __str__(self):
        return ("ชื่อพนักงาน = {}".format(self.name))
        
        
class Programmer(Employee):
    __departmentName = "Depatment Com"
    def __init__(self, name, salary, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__skill = skill
    
    def showData(self):
        super().showData()
        print("skill : {}".format(self.__skill))
        
     
emp1 = Programmer("emp1", 1000, "payhton")
emp1.showData()
print("รายได้ต่อปี : {}".format(emp1._getIncom()))


emp2 = Programmer("emp2", 2000, "swift")
emp2.showData()
print("รายได้ต่อปี : {}".format(emp2._getIncom(50)))






