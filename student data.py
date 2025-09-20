class Student:
    def __init__(self, name, address, marks, grade):
        self.name = name
        self.address = address
        self.marks = marks
        self.grade = grade


def save_to_file(students):
    file = open("students.txt", "w")
    file.write("Name | Address | Marks | Grade\n")
    for s in students:
        file.write(s.name + " | " + s.address + " | " +
                   s.marks + " | " + s.grade + "\n")
    file.close()
    print("\nData saved to students.txt")


def search_student(name):
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        if name in line:
            return line
    return None


n = int(input("Enter number of students: "))
students = []

for i in range(n):
    name = input("Enter name: ")
    address = input("Enter address: ")
    marks = input("Enter marks: ")
    grade = input("Enter grade: ")
    s = Student(name, address, marks, grade)
    students.append(s)

save_to_file(students)

j = input("Do you want to search the detail of the students(yes/no)?")
if j == "yes":
    search_name = input("\nEnter a name to search: ")
    result = search_student(search_name)

    if result:
        print("\nStudent found:\n" + result)
    else:
        print("\nStudent not found.")

elif j == "no":
    print("Thank you")

else:
    print("Please write yes or no.")
