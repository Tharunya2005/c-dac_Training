class Employee:
    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')

    def __iadd__(self,value):
        if type(value) not in (int, float, str):
            raise TypeError('works only with int, float, str')
        
        if type(value) in (int,float):
            self.salary += value
        else:
            self.name += value
        return self
    
    def __str__(self):
        return f'Employee(name = {self.name!r}, salary = {self.salary!r}) \n'
    
if __name__ == '__main__':
    e1 = Employee(name = 'Tharu', salary = 80000)
    print(e1)

    e1 += 90000
    print(e1)

    e1 += "nya"
    print(e1)