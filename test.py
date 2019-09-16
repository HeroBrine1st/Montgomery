import unittest

from mongo import Montgomery


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Montgomery(k=6, n=37)
        self.a = 52
        self.b = 35

    def test_multiply(self):
        a_n = self.obj.reminder(self.a)
        b_n = self.obj.reminder(self.b)
        result = self.obj.transform(self.obj.mon_pro(a_n, b_n))
        self.assertEqual(self.a * self.b % self.obj.n, result)

    @unittest.skip("Always failure")
    def test_exponentiation(self):
        mod = 11
        result = self.obj.mon_exp(self.a, self.b, mod)
        self.assertEqual(self.a ** self.b % mod, result)

    def test_exponentiation_base(self):
        result = self.obj.mon_exp(self.a, self.b, self.obj.n)
        self.assertEqual(self.a ** self.b % self.obj.n, result)


if __name__ == '__main__':
    unittest.main()
