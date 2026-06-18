import unittest
from task import Ticket_Pricing

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(Ticket_Pricing(5), 10)

    def test_multiple_digits(self):
        self.assertEqual(Ticket_Pricing(25), 20)

    def test_with_zero(self):
        self.assertEqual(Ticket_Pricing(70), 15)

    def test_child_under_5(self):
        self.assertEqual(Ticket_Pricing(3), 0)

    def test_infant(self):
        self.assertEqual(Ticket_Pricing(0), 0)

    def test_boundary_5(self):
        self.assertEqual(Ticket_Pricing(5), 10)

    def test_boundary_17(self):
        self.assertEqual(Ticket_Pricing(17), 10)

    def test_boundary_18(self):
        self.assertEqual(Ticket_Pricing(18), 20)

    def test_boundary_64(self):
        self.assertEqual(Ticket_Pricing(64), 20)

    def test_boundary_65(self):
        self.assertEqual(Ticket_Pricing(65), 15)

if __name__ == "__main__":
    unittest.main()
