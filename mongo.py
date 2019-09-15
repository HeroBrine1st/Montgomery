def euclide_ext(a, b):  # Расширенный алгоритм евклида. Списан с луа, должно работать
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y, a


def get_bit(num, pos):
    return (num & (1 << pos)) >> pos


class Montgomery:
    n: int
    k: int
    r: int
    r_inv: int
    n_inv: int

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.r = 2 ** k
        self.r_inv, self.n_inv, gcd = euclide_ext(self.r, self.n)
        self.n_inv = -self.n_inv  # Иначе не пройдет проверку
        if gcd != 1:
            raise ValueError("gcd(r,n) must be 1")
        if self.r * self.r_inv - self.n * self.n_inv != 1:
            raise ValueError(
                f"For ({self.r} that created from {2} ** {k},{n}) doesn't exists diophantine equation decision"
            )
        self.r_inv = self.r_inv % self.n

    def reminder(self, a):
        return a * self.r % self.n

    def transform(self, a):
        return a * self.r_inv % self.n

    def mon_pro(self, a_n, b_n):
        t = a_n * b_n
        u = (t + (t * self.n_inv % self.r) * self.n) >> self.k
        if u > self.n:
            u -= self.n
        return u

    def mon_exp(self, a: int, e: int, n: int):
        a = a * self.r % n
        x = self.r % n
        for i in reversed(range(0, e.bit_length())):
            x = self.mon_pro(x, x)
            if get_bit(e, i) == 1:
                x = self.mon_pro(x, a)
        return self.mon_pro(x, 1)
