import unittest
from task import Student_Grade_System

class TestAssignment(unittest.TestCase):

    def test1(self):
        self.assertEqual(Student_Grade_System("abc",50,50,50), "Average grade: 50.00, Status: Pass")

    def test2(self):
        self.assertEqual(Student_Grade_System("xyz",12,34,10), "Average grade: 18.67, Status: Fail")

    def test3(self):
        self.assertEqual(Student_Grade_System("preeti",90,80,70), "Average grade: 80.00, Status: Pass")

    def test_boundary_pass(self):
        self.assertEqual(Student_Grade_System("test",40,40,40), "Average grade: 40.00, Status: Pass")

    def test_boundary_fail(self):
        self.assertEqual(Student_Grade_System("test",39,39,39), "Average grade: 39.00, Status: Fail")

    def test_zero_grades(self):
        self.assertEqual(Student_Grade_System("test",0,0,0), "Average grade: 0.00, Status: Fail")

    def test_perfect_grades(self):
        self.assertEqual(Student_Grade_System("test",100,100,100), "Average grade: 100.00, Status: Pass")

if __name__ == "__main__":
    unittest.main()
