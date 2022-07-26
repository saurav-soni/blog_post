import logging

logging.basicConfig(filename='log_employee', level=logging.INFO, format='%(levelname)s:%(message)s')


class Employee:
    company = 'cleareye'
    domain = 'ai'

    def __init__(self, first, last, post):
        self.first = first
        self.last = last
        self.position = post
        self.salary = None

        logging.info(f"account created for: {self.fullname}, New Email: {self.email}")
        logging.info(f"{self.fullname} pay_grade: {self.paygrade()} after increment: {self.increment(200)}")

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@{self.company}.{self.domain}"

    def paygrade(self):
        if self.position == 'Junior':
            self.salary = 1000
        else:
            self.salary = 2000
        return self.salary

    def increment(self, value):
        return self.salary + value



emp_1 = Employee('Saurav', 'Kumar', 'Junior')
emp_2 = Employee('N.', 'Soni', 'Junior')
emp_3 = Employee('Nivin', 'Suresh', 'Senior')
