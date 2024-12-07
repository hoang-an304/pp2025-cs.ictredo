'''
Input functions:
• Input number of students in a class
• Input student information: id, name, DoB
• Input number of courses
• Input course information: id, name
• Select a course, input marks for student in this course
Listing functions:
• List courses
• List students
• Show student marks for a given course
'''

import os

students = []
courses = []
marks = {}

def input_students():
    student_nb = int(input('\ninput number of students: '))
    for i in range(student_nb):
        student_name = input('\nStudent name: ')
        student_id = input('Student ID: ')
        dob = input('Date of birth: ')
        students.append({'name' : student_name, 'id' : student_id, 'dob' : dob})

def input_courses():
    course_nb = int(input('\ninput number of courses: '))
    for i in range(course_nb):
        course_name = input('\nCourse name: ')
        course_id = input('Course ID: ')
        courses.append({'name' : course_name, 'id' : course_id})

def input_marks():
    course_id = input('\nEnter course id: ')
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        print("Course not found.")
        return
    print(f'Enter mark for course: {course['name']}')
    if course_id not in marks:
        marks[course_id] = {}
    for student in students:
        mark = float(input(f'Enter mark for student {student['name']} (ID: {student['id']}): '))
        marks[course_id][student['id']] = mark

def list_students():
    print('\nList of students:\n')
    print('--------------------')
    for student in students:
        print(f'Name: {student['name']} \nID: {student['id']} \nDate of birth: {student['dob']}')
        print('--------------------')

def list_courses():
    print('\nList of courses:\n')
    print('--------------------')
    for course in courses:
        print(f'Course name: {course['name']} \nCourse ID: {course['id']}')
        print('--------------------')

def course_marks():
    course_id = input('\nEnter course id: ')
    print('--------------------')
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        print("Course not found.")
        return
    for student in students:
        student_id = student['id']
        mark = marks[course_id].get(student_id, "N/A")
        print(f'\nStudent: {student['name']} \nID: {student['id']} \nMark: {mark}')
        print('--------------------')

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

while True:
    print(opt)
    n = int(input('opt: '))
    if n == 1:
        input_students()
    elif n == 2:
        input_courses()
    elif n == 3:
        input_marks()
    elif n == 4:
        list_students()
    elif n == 5:
        list_courses()
    elif n == 6:
        course_marks()
    elif n == 7:
        os.system('cls')
    else:
        print('\nexit\n')
        break
