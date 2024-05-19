from programmer import Programmer

emp1 = Programmer("emp1", 1000, "payhton")
emp1.showData()
print("รายได้ต่อปี : {}".format(emp1._getIncom()))


emp2 = Programmer("emp2", 2000, "swift")
emp2.showData()
print("รายได้ต่อปี : {}".format(emp2._getIncom(50)))