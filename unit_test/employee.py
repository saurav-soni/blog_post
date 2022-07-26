
class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, salary: int):
        self.first = first
        self.last = last
        self.sal = int(salary)

    @property
    def email(self):
        return f"{self.first}.{self.last}@cleareye.ai"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def raise_salary(self):
        self.sal = int(self.sal * self.raise_amt)
