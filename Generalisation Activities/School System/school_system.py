class Person:
    def __init__(self, name, dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender

    def display_details(self):
        print(f"Hello, my name is {self.name}, my birth date is {self.dob} and my gender is {self.gender}")

class Teacher(Person):
    def __init__(self, name, dob, gender, staffid, subject):
        super().__init__(name, dob, gender)
        self.subject = subject
        self.staffid = staffid
        

    def display_tchrdetails(self):
        print(f"I teach {self.subject}, and my staff id is {self.staffid}")

class Student(Person):
    def __init__(self, name, dob, gender, faculty, id):
        super().__init__(name, dob, gender)
        self.faculty = faculty
        self.id = id
        
    def display_stdtdetails(self):
        print(f"My student id is {self.id} and I study {self.faculty}")

class Parent(Person):
    def __init__(self, name, dob, gender, work, childname, workid):
        super().__init__(name, dob, gender)
        self.work = work
        self.workid = workid
        self.childname = childname

    def display_prntdetails(self):
        print(f"I am a {self.work}, my child's name is {self.childname} and my work id is {self.workid}")