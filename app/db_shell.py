from app.models import *

all_emps = Employee.objects.all()
# print(all_emps)

emp1 = Employee.objects.get(id=1)
# print(emp1)

# for emp in all_emps:
#     print(emp.mob_num)

# emps = Employee.objects.filter(first_name__startswith="e")
# print(emps)

emps = Employee.objects.filter(first_name__in=["emp1", "emp2"])
print(emps)