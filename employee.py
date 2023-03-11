# import datetime

class Employee:
    
    num_of_employees = 0
    raise_amount = 1.04
    
    def __init__ (self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
                
         #increaments each time and instance / employee is created
        Employee.num_of_employees += 1 
    #alllows an authomatic update to the email anytime the fname or lname is changed 
    @property
    def email(self):
        return ('{}.{}@company.com'.format(self.fname, self.lname))
    
    def fullName(self):
        return ('{} {}'.format(self.fname, self.lname))
    
    def apply_raise(self):
        self.pay = int((self.pay * self.raise_amount)) #Employee.raise_amount
        
    #static method to check if a date is a work day or not
    @staticmethod
    def is_workday(day): 
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname,self.pay)
    
    
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)


