from subjects import Subject

list_of_subjects = []

def Start():
        print("Welcome to the subject management system")
        while True:
            print("1. Add Subject")
            print("2. View Subjects")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                add_subject()
            elif choice == '2':
                view_subjects()
            elif choice == '3':
                break


def add_subject():
    sbjctname = input("Enter subject name: ")
    sbjctyearlvl = input("Enter subject year level: ")
    sbjctclscode = input("Enter subject code: ")
    sbjctstudentno = input("Enter number of students: ")
    subject = Subject(sbjctname, sbjctyearlvl, sbjctclscode, sbjctstudentno)
    list_of_subjects.append(subject)
    print(f"Subject {sbjctname} added")



def view_subjects():
    if list_of_subjects == []:
        print("No subjects entered yet")
        return
    selected_subject = input("Enter the subject name to view: ")
    for subject in list_of_subjects:
        if subject.name == selected_subject:
            print(f"Subject Name: {subject.name}")
            print(f"Year Level: {subject.yearlvl}")
            print(f"Code: {subject.clscode}")
            print(f"Number of Students: {subject.studentno}")
        else:
            print("Subject not found")


Start()


