import unittest
import GuessingNumber


class TestGuessingNumber(unittest.TestCase):
    def test_check_guess1(self):
        result = GuessingNumber.check_guess()
        self.assertEqual(result, 'You are genius')

    def test_check_guess2(self):
        result = GuessingNumber.check_guess()
        self.assertEqual(result, 'Try again')

    def test_check_guess3(self):
        result = GuessingNumber.check_guess()
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
