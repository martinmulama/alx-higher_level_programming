import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_max_integer(self):
        """Test case with a list of positive integers"""
        self.assertEqual(max_integer([1, 3, 5, 7, 9]), 9)

        """Test case with a list of negative integers"""
        self.assertEqual(max_integer([-1, -3, -5, -7, -9]), -1)

        """Test case with a list containing a mixture of positive and negative integers"""
        self.assertEqual(max_integer([-1, 3, -5, 7, -9]), 7)

        # Test case with an empty list
        self.assertIsNone(max_integer([]))

        # Test case with a list containing a single element
        self.assertEqual(max_integer([42]), 42)

        # Test case with a list containing duplicate elements
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_max_integer_invalid_input(self):
        # Test case with a list containing non-integer values
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4, 5])

        # Test case with a list containing a mixture of integer and non-integer values
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4, 5])

        # Test case with a list containing non-integer values and None
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4, 5])

if __name__ == '__main__':
    unittest.main()
