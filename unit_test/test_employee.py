import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Saurav', 'Kumar', 1000)
        self.emp_2 = Employee('Nan', 'Soni', 2000)

    def tearUp(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Saurav.Kumar@cleareye.ai')
        self.assertEqual(self.emp_2.email, 'Nan.Soni@cleareye.ai')

        self.emp_1.first = 'Mr'
        self.emp_2.first = 'Miss'

        self.assertEqual(self.emp_1.email, 'Mr.Kumar@cleareye.ai')
        self.assertEqual(self.emp_2.email, 'Miss.Soni@cleareye.ai')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Saurav Kumar')
        self.assertEqual(self.emp_2.fullname, 'Nan Soni')

        self.emp_1.first = 'Mr'
        self.emp_2.first = 'Miss'

        self.assertEqual(self.emp_1.fullname, 'Mr Kumar')
        self.assertEqual(self.emp_2.fullname, 'Miss Soni')

    def test_raise_salary(self):
        self.emp_1.raise_salary()
        self.emp_2.raise_salary()

        self.assertEqual(self.emp_1.sal, 1050)
        self.assertEqual(self.emp_2.sal, 1050)


if __name__ == '__main__':
    unittest.main()
