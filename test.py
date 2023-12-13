class Employee:
    """Common base class for all employees"""
    empCount = 0
 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1
 
    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")
 
    def display_employee(self, display_option=0):
        if display_option % 3 == 0:
            print("Name : ", self.name)
        elif display_option % 3 == 1:
            print("Salary: ", self.salary)
    
 
    def __del__(self):
        Employee.empCount -= 1
 
    def update_salary(self, new_salary):
        self.salary = new_salary
 
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status
 
    def display_task(self, status):
        print(f"Tasks with status {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)
 
 
class Manager(Employee):
    """Class representing a manager, inheriting from Employee"""
    mgr_count = 0
 
    def __init__(self, name, salary, department):
        department='D12'
        super().__init__(name, salary)
        self.department = department
        Manager.mgr_count += 1
    # valoarea lui x, in cazul meu este 8 => x%3=2, ceea ce rezulta ca va afisa departamentul fiecarui manager
    def display_employee(self, display_option=0):
        if display_option % 3 == 0:
            print("Name : ", self.name)
        elif display_option % 3 == 1:
            print("Salary: ", self.salary)
        elif display_option % 3 == 2:
            print("Department: ", self.department)
 
    def display_man_count(self):
        "Displays the number of managers"
        print(f"Total number of manager(s) is {Manager.mgr_count}")
 
 #valoarea lui y, in cazu meu este y=11 =>y/3=3, ceea ce rezulta ca vom creea 3 obiecte de tip manager 
manager1 = Manager("Vasile", 90000, "D12")
manager2 = Manager("Traian", 100000, "D12")
manager3 = Manager("Adrian", 80000, "D12")

 #aici nu am avut vreo restrictie, asa ca am creeat 3 angajati
employee1 = Employee("Marius", 50000)
employee2 = Employee("Cristian", 55000)
employee3 = Employee("Sebastian", 55000) 
for obj in [manager1, manager2, manager3, employee1, employee2]: #pentru a afisa numele, departamentul sau salariul fiecarui manager(in cazul meu departamentul)
    obj.display_employee(8)  #numarul de literele al numelui
 
employee1.display_emp_count() #afisarea nr de angajati
manager1.display_man_count()  #afisarea nr. de manageri