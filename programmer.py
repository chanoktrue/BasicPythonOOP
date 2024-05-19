from employee import Employee

class Programmer(Employee):
    __departmentName = "Depatment Com"
    def __init__(self, name, salary, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__skill = skill
    
    def showData(self):
        super().showData()
        print("skill : {}".format(self.__skill))