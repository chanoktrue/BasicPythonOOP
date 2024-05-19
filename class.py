
# Inheritance
class Employee:
    # class variable
    minSalary = 10000
    maxSalary = 30000
    companyName = "Company XYZ"
    
    def __init__(self, name, salary, department):
        # instance variable
        self.name = name
        self.salary = salary
        self.department = department
        
    def showData(self):
        print("staff name = ", self.name)
        print("salary = ", format(self.salary))
        print("department :", self.department)
        
        
class Programmer(Employee):
    __departmentName = "Depatment Com"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
     
com = Programmer("roj", 1000)
com.showData()



