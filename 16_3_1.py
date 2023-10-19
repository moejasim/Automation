
#1
def insert_element(new_cloth, index=0):
    clothes =["socks", "shirt", "skirt", "scarf"]
    clothes.insert(index,new_cloth)
    print (clothes)

insert_element("hat",index=2)
insert_element("glasses",index=-1)
insert_element("bag")
#2
employee_shift=["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
def replace_employee(employee_list, old_employee, new_employee):
    index=employee_shift.index(old_employee)
    employee_shift.remove(old_employee)
    employee_shift.insert(index,new_employee)
    print(employee_shift)

replace_employee(employee_shift, "Kelly", "Maria")
