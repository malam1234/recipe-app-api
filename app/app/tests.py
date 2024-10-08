"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """"Test add number."""
        res = calc.add(3, 4)

        self.assertEqual(res, 7)

    def test_sub_numbers(self):
        """ Subtract number"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, -5)
