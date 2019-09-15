import unittest

from mongo import Montgomery


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Montgomery(k=4, n=7)
        self.a = 5
        self.b = 3

    def test_multiply(self):
        a_n = self.obj.reminder(self.a)
        b_n = self.obj.reminder(self.b)
        result = self.obj.transform(self.obj.mon_pro(a_n, b_n))
        self.assertEqual(self.a * self.b % self.obj.n, result)

    def test_exponentiation(self):
        mod = 11
        result = self.obj.mon_exp(self.a, self.b, mod)
        self.assertEqual(self.a ** self.b % mod, result)


if __name__ == '__main__':
    unittest.main()
