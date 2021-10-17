class Employee:
    no_of_leaves = 8
    pass

nitin = Employee()
aayush = Employee()

nitin.name = "Nitin"
nitin.salary = 455
nitin.role = "Instructor"

aayush.name = "aayush"
aayush.salary = 4554
aayush.role = "Student"
print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)