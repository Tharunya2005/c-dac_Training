class person:
    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')

    def print(self):
        print(f'name = {self.name}')
        print(f'city = {self.city}')

class student(person):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rollno = kwargs.get('rollno')
        self.cgpa = kwargs.get('cgpa')

    def print(self):
        super().print()
        print(f'Rollno = {self.rollno}')
        print(f'cgpa = {self.cgpa}')

if __name__ == '__main__':
    p1 = person(name = 'Tharu', city='Salem')
    p1.print()
    print('-'*20)

    s1 = student(name= 'meena', city = 'salem', rollno = 1, cgpa = 9.0)
    s1.print()
