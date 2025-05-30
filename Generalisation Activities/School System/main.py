from school_system import Person, Teacher, Student, Parent

parent1 = Parent("Bob", "19/02/1989", "Male", "Construction Worker", "Timmy", 291012)
person1 = Person("Victor", "24/10/2005", "Male")
student1 = Student("Timmy", "02/10/2009", "Male", "Computer Science", 921021)
teacher1 = Teacher("Scott", "02/02/1877", "Male", 941292, "Computer Science")

person1.display_details()
parent1.display_details()
student1.display_details()
teacher1.display_details()

parent1.display_prntdetails()
student1.display_stdtdetails()
teacher1.display_tchrdetails()