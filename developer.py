from employee import Employee

class Developer(Employee):
    raise_amount = 1.10 
    
    def __init__(self, fname, lname, pay, progr_lang):
        super().__init__(fname, lname, pay)
        self.progr_lang = progr_lang
            
                