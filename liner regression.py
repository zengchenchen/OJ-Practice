import math


def gradient_descent(x, y):
    alpha = 0.01
    m = len(x)
    theta0 = 0
    theta1 = 0
    a = 0
    b = 0
    cf = 0
    for i in range(0, len(x)):
        cf = cf + (theta0 + theta1 * x[i] - y[i])**2
    while math.sqrt(cf) > 1.0:

        for i in range(0, len(x)):
            a = a + theta0 + theta1 * x[i] - y[i]
            b = b + (theta0 + theta1 * x[i] - y[i]) * x[i]
        theta0, theta1 = theta0 - (alpha / m) * a, theta1 - (alpha / m) * b
        a = 0
        b = 0
        cf = 0
        for i in range(0, len(x)):
            cf = cf + (theta0 + theta1 * x[i] - y[i])**2
        print(math.sqrt(cf), theta0, theta1)
    return theta0, theta1


print(gradient_descent([-0.5, -1 / 6, 1 / 6, 0.6], [11, 12, 13, 14]))  # 特征缩放
