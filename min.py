x = 0.0
y = 0.0
f_der_x = float(36 * x ** 5 + 8 * x ** 3 * y ** 2 + 20 * x + 6 * y - 6)
f_der_y = float(4 * x ** 4 * y + 6 * x + 20 * y)
lam = 0.001
i = 0
while i < 10000:
    x = x - lam * f_der_x
    y = y - lam * f_der_y
    f_der_x = float(36 * x ** 5 + 8 * x ** 3 * y ** 2 + 20 * x + 6 * y - 6)
    f_der_y = float(4 * x ** 4 * y + 6 * x + 20 * y)
    i += 1
f = 6 * x ** 6 + 2 * x ** 4 * y ** 2 + 10 * x ** 2 + 6 * x * y + 10 * y ** 2 + - 6 * x + 4
print(float(f))
