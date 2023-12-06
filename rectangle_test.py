import unittest
import rectangle
class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle.area(5, 10), 50)
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertEqual(rectangle.area(-5, 10), -50)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)
        self.assertEqual(rectangle.perimeter(0, 10), 20)
        self.assertEqual(rectangle.perimeter(-5, 10), 10)


if __name__ == '__main__':
    unittest.main()
