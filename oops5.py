class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f" The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


nitin = Employee("Nitin", 255, "Instructor")
aayush = Employee("aayush", 455, "student")
karan = Employee.from_dash("Karan-480-student")

print(karan.no_of_leaves)
# aayush.change_leaves(34)
#
# print(nitin.no_of_leaves)