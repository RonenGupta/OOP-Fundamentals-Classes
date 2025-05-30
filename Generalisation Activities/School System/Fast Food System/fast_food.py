class Employee:
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
    
    def clock_in(self):
        print(f"You have now clocked in.")
        
