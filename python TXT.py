from numpy import *
train_x = []
train_y = []
fileIn = open('/Users/cengchenchen/Downloads/python/testset.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split(',')
    train_x.append([float(lineArr[0]), float(lineArr[1])])
    train_y.append([float(lineArr[2])])
    x = mat(train_x)
    y = mat(train_y)
