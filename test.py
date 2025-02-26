import unittest
from unittest.mock import patch
from io import StringIO
import sys
import math
from calculator import main

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = sys.__stdout__

    def test_square_root(self):
        # Test case for square root function
        user_input = ["1", "25", "5"] 
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            main()
        output = self.held_output.getvalue()
        self.assertIn("Square root of 25.0 is 5.0", output)

    def test_factorial(self):
        # Test case for factorial function
        user_input = ["2", "5", "5"]
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            main()
        output = self.held_output.getvalue()
        self.assertIn("Factorial of 5 is 120", output)

    def test_natural_logarithm(self):
        # Test case for natural logarithm function
        user_input = ["3", "2.718", "5"]
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            main()
        output = self.held_output.getvalue()
        self.assertIn("Natural logarithm of 2.718 is", output)

    def test_power_function(self):
        # Test case for power function
        user_input = ["4", "2", "3", "5"]
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            main()
        output = self.held_output.getvalue()
        self.assertIn("2.0 raised to the power of 3.0 is 8.0", output)

    def test_invalid_choice(self):
        # Test case for invalid choice handling
        user_input = ["6", "5"]
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            main()
        output = self.held_output.getvalue()
        self.assertIn("Invalid choice. Please select a valid option (1-5).", output)

if __name__ == '__main__':
    unittest.main()
