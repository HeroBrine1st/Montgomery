def euclide_ext(a, b):  # Расширенный алгоритм евклида. Списан с луа, должно работать
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y, a


def extended_euclidean(a, b):
    pass


def modular_inversion(a, m):
    x, y, d = euclide_ext(a, m)
    if d == 1:
        if x < 0:
            x = x % m
        return x
    raise ValueError("gcd(a,m) must be 1")


a = 6
b = 5
r = 16  # Не трогать, иначе может сломаться и умножение
n = 7
##########
a_n = a * r % n
b_n = b * r % n
r_inv, n_inv, gcd = euclide_ext(r, n)
if gcd != 1:
    raise ValueError("gcd(r,n) must be 1")
if r * r_inv + n * n_inv != 1:
    raise ValueError("For (%s,%s) doesn't exists diophantine equation decision" % (r, n))
r_inv = r_inv % n


def mon_pro(a_n, b_n):
    t = a_n * b_n
    u = (t + (t * n_inv % r) * n) / r
    while u >= n:
        u -= n
    return u


def get_bit(num, pos):
    return (num & (1 << pos)) >> pos


def mon_exp(a: int, e: int, n: int):
    a_n = a * r % n
    x_n = r % n
    for i in range(e.bit_length() - 1, -1, -1):
        x_n = mon_pro(x_n, x_n)
        if get_bit(e, i) == 1:
            x_n = mon_pro(x_n, a_n)
        print(x_n, i)
    return mon_pro(x_n, 1)
    # return x_n


print("Mul")  # Тестовое умножение - проверка подобранных значений
reminder = mon_pro(a_n, b_n)
result = reminder * r_inv % n
print("reminder", reminder)
print(result)
print(a * b % n)

print("Exp")  # Возведение в степень
reminder = mon_exp(a, b, n)
result = reminder * r_inv % n
print("reminder", reminder)
print(result)
print(a ** b % n)
