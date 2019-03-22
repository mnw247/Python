import unittest
from myHomework import reverseList, isPalindrome, coins, factorial, fib
class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList(2,4,-3), [-3,4,2])

class isPalindromeTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
       return self.assertEqual(isPalindrome("rabbit", False))

class coinsTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coinsTest, ?)

class factorialTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorialTest, ?)

class fibTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(fibTest, ?)
if __name__ == "__main__":
    unittest.main()