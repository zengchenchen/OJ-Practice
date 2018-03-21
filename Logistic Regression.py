from numpy import *
import re
train_x = []
train_y = []
fileIn = open('/Users/cengchenchen/Downloads/python/testset.txt')
for line in fileIn.readlines():
    lineArr = line.split()
    lineArr1 = lineArr[1:]
    train_x.append([1, float(lineArr1[0]), float(lineArr1[1])])
    train_y.append(float(lineArr1[2]))
    x = mat(train_x)
    y = mat(train_y).transpose()
theta0 = 0
theta1 = 0
theta2 = 0
a = 0
b = 0
c = 0
cf = 0
alpha = 0.01


def f1(z):
    return 1 / (1 + exp(-z))


theta = mat([[theta0], [theta1], [theta2]])
for i in range(0, x.shape[0]):
    cf = cf + train_y[i] * log(f1(theta.T * (mat([train_x[i]]).T))) + \
        (1 - train_y[i]) * log(1 - f1(theta.T * (mat([train_x[i]]).T)))
cf = (-1 / 100) * cf
while cf > 0.1:
    for i in range(0, x.shape[0]):
        a = a + (f1(theta.T * (mat([train_x[i]]).T)) - train_y[i])
        b = b + (f1(theta.T * (mat([train_x[i]]).T)
                    ) - train_y[i]) * train_x[i][1]
        c = c + (f1(theta.T * (mat([train_x[i]]).T)
                    ) - train_y[i]) * train_x[i][2]
    theta0, theta1, theta2 = theta0 - alpha * \
        a, theta1 - alpha * b, theta2 - alpha * c
    a = 0
    b = 0
    c = 0
    cf = 0
    for i in range(0, x.shape[0]):
        cf = cf + train_y[i] * log(f1(theta.T * (mat([train_x[i]]).T))) + (
            1 - train_y[i]) * log(1 - f1(theta.T * (mat([train_x[i]]).T)))
    cf = (-1 / 100) * cf
print(cf)
