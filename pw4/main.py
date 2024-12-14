import os
from domains.marks import Management


opt = '''
---Student mark management---

1. input student info
2. input course info
3. input marks
4. list students
5. list courses
6. list marks
7. calculate average gpa
8. clean screen
9. exit '''

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
        manage.calculate_gpa()
    elif n == 8:
        os.system('cls')
    else:
        print('\nexit\n')
        break