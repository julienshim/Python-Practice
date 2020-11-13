import unittest

from other_assertion_types import is_funny, laugh
from activities import eat


class OtherAssertionTypesTest(unittest.TestCase):
    def test_is_funny_tim(self):
        # self.assertEqual(is_funny("tim"), False)
        self.assertFalse(is_funny("tim"), "tim should not be funny")

    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

    def test_eat_healthy_boolean(self):
        """"is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")


if __name__ == "__main__":
    unittest.main()
