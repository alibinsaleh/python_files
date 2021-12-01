import sys

students_dict = {
        'Ali':    {'Computer': 95, 'Physics': 84, 'Chemistry': 55},
        'Ahmed':  {'Computer': 63, 'Physics': 83, 'Chemistry': 36},
        'Majed':  {'Computer': 97, 'Physics': 77, 'Chemistry': 100},
        'Naser':  {'Computer': 87, 'Physics': 65, 'Chemistry': 99},
        'Waleed': {'Computer': 54, 'Physics': 49, 'Chemistry': 56}
}

def findCourseAverageGrades(course):
    total = 0
    for k, v in students_dict.items():
        total = total + v.get(course, 0)
        print(k, v.get(course))
    count = len(students_dict)
    print(f'{course} Average: {total / count}')


if len(sys.argv) < 2:
    print("Usage: python3 students_dict.py [course name]. Ex: python3 students_dict.py Computer")
    sys.exit()
else:
    findCourseAverageGrades(str(sys.argv[1]))
