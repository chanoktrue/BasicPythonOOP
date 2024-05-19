
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