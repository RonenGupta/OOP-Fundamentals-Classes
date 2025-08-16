import datetime

class Employee:
    def __init__(self, name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
        self.clock_in_time = datetime.datetime.now()
        self.clock_out_time = datetime.datetime.now()
    
    def clock_in(self):
        print(f"You have now clocked in at {self.clock_in_time}.")
        return self.clock_in_time

    def clock_out(self):
        print(f"You have now clocked out at {self.clock_out_time}.")
        return self.clock_out_time

    def get_pay(self):
        duration = self.clock_out_time - self.clock_in_time
        self.shift_hours = duration.total_seconds() / 3600
        total_pay = self.shift_hours * 11.95
        print(f"Your total pay is {total_pay}! Thanks for working!")

class Cashier(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time, register_number):
        super().__init__(name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time)
        self.register_number = register_number

    def process_order(self, order_id):
        print(f"{self.name} processed order id #{order_id} at register {self.register_number}")

class Cook(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time, cook_id):
        super().__init__(name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time)
        self.cook_id = cook_id

    def cook_order(self, order_id):
        print(f"{self.name} with order id #{self.cook_id} cooked order #{order_id}")

    def get_pay(self):
        duration = self.clock_out_time - self.clock_in_time
        self.shift_hours = duration.total_seconds() / 3600
        total_pay = self.shift_hours * 15.00
        print(f"Your total pay is {total_pay}! Thanks for working!")

class Cleaner(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time, cleaner_id):
        super().__init__(name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time)
        self.cleaner_id = cleaner_id

    def clean_area(self, area):
        print(f"{self.name} with cleaner id #{self.cleaner_id} has cleaned area: {area.capitalize()}!")

    def get_pay(self):
        duration = self.clock_out_time - self.clock_in_time
        self.shift_hours = duration.total_seconds() / 3600
        total_pay = self.shift_hours * 9.00
        print(f"Your total pay is {total_pay}! Thanks for working!")

class FryCook(Cook):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time, cook_id, food):
        super().__init__(name, employee_id, hourly_wage, shift_hours, clock_in_time, clock_out_time, cook_id)
        self.food = food

    def burger(self, order_id):
        print(f"Fry Cook {self.name} with #{self.cook_id} has cooked order id #{order_id}'s food choice: {self.food.capitalize()}")



