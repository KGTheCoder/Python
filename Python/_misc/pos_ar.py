class Employee:
    def GetEmpployeeID(self, name):
        print(f"The Employee ID of {name} ", 1234)

empObj = Employee()
print(empObj.GetEmpployeeID("Mr. K"))