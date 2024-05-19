
# Access Modifier 
# 1.public
# 2.Protected = _
# 3.Private = __

# Inheritance
class Employee:
    # class variable
    minSalary = 10000
    maxSalary = 30000
    companyName = "Company XYZ"
    
    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self._salary = salary
        self._department = department
        
    def _showData(self):
        print("staff name = ", self.__name)
        print("salary = ", format(self._salary))
        print("department :", self._department)
            
com = Employee("roj", 1000, "Dep")
com._name = "tset"
com._showData()

