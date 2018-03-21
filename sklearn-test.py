import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# KNN分类：无参分类，样本与测试点的距离为欧氏距离((x1-y1)**2+()+,...,+())**0.5
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import preprocessing
# 数据预处理
from sklearn.datasets.samples_generator import make_classification
# 自己创造分类数据
from sklearn.svm import SVC

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
# iris_y 本身是0，1数字，不需要特殊处理
# print(iris_X)
# print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(
    iris_X, iris_y, test_size=0.3)
# print(X_train, y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print(knn.predict(X_test))
print(y_test)

load_data = datasets.load_boston()
data_x = load_data.data
data_y = load_data.target
model = LinearRegression()
model.fit(data_x, data_y)
# print(model.predict(data_x[:10, :]))
# print(data_y[:10])
print(model.coef_)  # coef_:一次项系数
print(model.intercept_)  # 截距
print(model.get_params())
print(model.score(data_x, data_y))

x, y = datasets.make_regression(
    n_samples=100, n_features=1, n_targets=1, noise=0)
plt.scatter(x, y)
# 画出散列点
plt.show()

a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)
print(a)
# array是数组，也可以看做是矩阵，但是矩阵相乘可以用*，数组相乘用.dot()
# b = np.matrix('1 2 7; 3 4 8; 5 6 9') b是矩阵
print(preprocessing.scale(a))
# preprocessing包括：标准化.scale(),特征值缩放到一个范围.MinMaxScaler(),正则化.normalize(),二值化.Binarizer()
X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

X = preprocessing.scale(X)    # normalization step
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
