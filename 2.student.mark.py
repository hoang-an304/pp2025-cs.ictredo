import os

class Students:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

class Courses:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        nb_students = int(input('\nEnter number of students: '))
        for i in range(nb_students):
            name = input('Enter name: ')
            id = input('Enter ID:')
            dob = input('Enter date of birth: ')
            self.students.append(Students(name, id, dob))

    def input_courses(self):
        nb_courses = int(input('\nEnter number of courses: '))
        for i in range(nb_courses):
            name = input('Enter name: ')
            id = input('Enter ID:')
            self.courses.append(Courses(name, id))

    def input_marks(self):
        course_id = input("\nEnter course ID to input marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Course not found.")
            return
        print(f"Entering marks for course: {course.name}")
        if course_id not in self.marks:
            self.marks[course_id] = {}
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} (ID: {student.id}): "))
            self.marks[course_id][student.id] = mark

    def list_students(self):
        print('\nList of students: \n--------------------')
        for student in self.students:
            print(f'Name: {student.name} \nID: {student.id} \nDate of birth: {student.dob} \n--------------------')

    def list_courses(self):
        print('\nList of courses: \n--------------------')
        for course in self.courses:
            print(f'Name: {course.name} \nID: {course.id} \n--------------------')

    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Course not found.")
            return
        print(f"\nMarks for course: {course.name}")
        if course_id not in self.marks or not self.marks[course_id]:
            print("No marks available for this course.")
            return
        for student in self.students:
            mark = self.marks[course_id].get(student.id, "N/A")
            print(f"Student: {student.name} (ID: {student.id}), Mark: {mark}")

opt = '''
choose operation:
1. input student info
2. input course info
3. input marks
4. list students
5. list courses
6. list marks
7. clean screen
8. exit '''

manage = Management()
while True:
    print(opt)
    n = int(input('opt: '))
    if n == 1:
        manage.input_students()
    elif n == 2:
        manage.input_courses()
    elif n == 3:
        manage.input_marks()
    elif n == 4:
        manage.list_students()
    elif n == 5:
        manage.list_courses()
    elif n == 6:
        manage.course_marks()
    elif n == 7:
        os.system('cls')
    else:
        print('\nexit\n')
        break