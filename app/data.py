class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.first = last
        self.first = pay

    def fullname(self, first, last):
        return f'{first} {last}'


emp_1 = Employee('john', 'kalisa', 5000)
print(emp_1)
