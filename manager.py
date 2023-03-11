from employee import Employee
            
class Manager(Employee):
    
    def __init__(self, fname, lname, pay, employees = None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.num_of_employees = [] #it will returnn an empty strig if there're no employees added
        else:
             self.employees = employees
             
    #method to add employees to a manager subclass of Employee
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
     #method to remove employees from a manager
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    #to print the list of all emps under this mgr
    def print_employees(self):
        for emp in self.employees:
            print(emp.fullName(), 'is under' + ' ' f'{self.fullName()}')
        
    
   