class Student():
    def __init__(self):
        self.students = []
        self.read_data()

    def enroll(self, name):
        self.students.append(name)

    def show_all(self):
        for l in self.students:
            print(l)

    def read_data(self):
        try:
            with open('test_data.txt', 'r') as f:
                for i in f.readlines():
                    self.students.append(i.strip())
        except:
            print('Sorry, file does not exist, I will create it.')
            f = open('test_data.txt', 'w')
        finally:
            f.close()


    def store(self):
        with open('test_data.txt', 'w') as f:
            for l in self.students:
                f.write(l+'\n')
            f.close()


def main():
    student = Student()
    print('Want to enroll some students now? (y/n):')
    ans = input()
    if ans.lower() == 'y':
        while True:
            print('Enter student name (none to finish):')
            n = input()
            if n.lower() == 'none':
                break
            student.enroll(n)

    #x.enroll('Saleh')
    #x.enroll('Waheed')
    #x.enroll('Kamal')
    student.store()
    student.show_all()


if __name__ == "__main__":
    main()
