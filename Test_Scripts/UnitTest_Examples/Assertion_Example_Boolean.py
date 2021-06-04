import unittest


class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9, "Both value are equal")

    def test2(self):
        self.assertNotEqual(5 * 1, 10)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is True")

    def test4(self):
        self.assertTrue(4 + 6 == 10, "assertion Pass")

    def test5(self):
        self.assertIn(3, [1, 2, 3])

    def test6(self):
        self.assertNotIn(6, range(5))


if __name__ == '__main__':
    unittest.main()
