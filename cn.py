zero = lambda f: lambda x: x
succ = lambda n: lambda f: lambda x: f(n(f)(x))
pred = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)


def mult_(a, b):
    def mult_iter(n, k, result):
        if n == 0:
            return result
        elif n & 1 == 0:
            return mult_iter(n >> 1, k + k, result)
        else:
            return mult_iter(n - 1, k, k + result)
    return mult_iter(b, a, 0)


def plus_(a, b):
    if b == 0:
        return a
    elif b & 1 == 0:
        return plus_(a + (b >> 1), b >> 1)
    else:
        return plus_(a + 1, b - 1)


def plus(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))


def mult(m, n):
    return lambda f: m(f(n))


def pow(b, e):
    return e(b)


one = succ(zero)
two = succ(one)
three = succ(two)
b = lambda f: lambda x: f(f(x))


def church_numeral_to_int(f):
    return f(lambda x: x + 1)(0)


print(church_numeral_to_int(zero))
print(church_numeral_to_int(one))
print(church_numeral_to_int(two))
print(church_numeral_to_int(three))
print(church_numeral_to_int(plus(two, three)))
print(church_numeral_to_int(pow(two, three)))
print(church_numeral_to_int(b))
print(church_numeral_to_int(pred(two)))

