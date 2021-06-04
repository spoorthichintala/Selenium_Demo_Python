import unittest


class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertGreater(4, 3, "First Value Greater than Second value")

    def test2(self):
        self.assertGreaterEqual(4, 4, "First Value Greater and = than Second value")

    def test3(self):
        self.assertLess(3, 4, "First Value Lesser than Second value")

    def test4(self):
        self.assertLessEqual(3, 3, "First Value Lesser and = than Second value")

    def test5(self):
        self.assertRegex("Welcome Pooja", "Pooja")


if __name__ == '__main__':
    unittest.main()
