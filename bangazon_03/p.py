from departments import *
from employees import *


hr_department = HR("Human Resources", "Angela", 2)
admin_department = Admin("Administration", "Kayla", 4)
sales_department = Sales("Sales", "Max", 6)
it_department = InfoTech("Information Technogology", "Adam", 1)
print(hr_department.name, hr_department.supervisor, hr_department.employee_count)
print(admin_department.name, admin_department.supervisor, admin_department.employee_count)
print(sales_department.name, sales_department.supervisor, sales_department.employee_count)
print(it_department.name, it_department.supervisor, it_department.employee_count)

hr_department.add_policy("1.1", "Policy 1.1")
hr_department.add_policy("1.2", "Policy 1.2")
print(hr_department.policies)
print(sales_department.meet())
print(it_department.budget)
print(sales_department.budget)

##############################################