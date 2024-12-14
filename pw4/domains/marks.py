from domains.students import Students
from domains.courses import Courses
from math import floor
import numpy

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
            id = input('Enter ID: ')
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
            rounded_mark = floor(mark * 10) / 10
            self.marks[course_id][student.id] = rounded_mark

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

    def calculate_gpa(self):
        student_id = input('\nEnter student ID to calculate GPA: ')
        student = next((s for s in self.students if s.id == student_id), None)
        if not student:
            print('Student not found.')
            return
        scores = []
        for course_id, student_marks in self.marks.items():
            if student_id in student_marks:
                scores.append(student_marks[student_id])
            if not scores:
                print(f'No marks for student {student.name} (ID: {student.id})')
                return
            scores_arr = numpy.array(scores)
            average_gpa = numpy.mean(scores_arr)
            print(f'The average GPA of student {student.name} (ID: {student.id}) is: {average_gpa}')