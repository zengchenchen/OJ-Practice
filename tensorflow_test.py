import tensorflow as tf
import numpy as np

## 入门小例子 ##
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

## Session() ##
import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])
product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

with tf.Session() as sess1:
    result = sess1.run(product)
    print(result)

## variables ##
import tensorflow as tf

state = tf.Variable(1, name='counter')
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        sess.run(update)
    print(sess.run(state))

## placehoder ##
import tensorflow as tf

input_1 = tf.placeholder(tf.float32, [1, 3])
input_2 = tf.placeholder(tf.float32, [3, 1])
input_3 = tf.placeholder(tf.float32)
input_4 = tf.placeholder(tf.float32)
input_5 = tf.placeholder(tf.float32, [1, None])
input_6 = tf.placeholder(tf.float32, [None, 1])

output = tf.matmul(input_1, input_2)
output1 = tf.multiply(input_3, input_4)
output2 = tf.matmul(input_5, input_6)


with tf.Session() as sess:
    print(sess.run(output, feed_dict={
          input_1: [[1, 2, 3]], input_2: [[1], [2], [3]]}))
    print(sess.run(output1, feed_dict={input_3: [3.], input_4: [4.]}))
    print(sess.run(output1, feed_dict={input_3: 3, input_4: 4}))
    print(sess.run(output2, feed_dict={
          input_5: [[1, 2, 3]], input_6: [[1], [2], [3]]}))

## 神经网络案例 ##
## 神经网络案例 ##
## 神经网络案例 ##
## 神经网络案例 ##
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
# digits存储了数字识别的数据，包含了1797条记录，每条记录又是一个8行8列的矩阵
# 随机划分train datas和test datas
# 标签二值化，将标签转化成0，1

# 搭建神经网络层并绘制分类器图形，利用tensorboard绘制神经网路


def add_layer(inputs, in_size, out_size, n_layer=None, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope('layer'):
        with tf.name_scope('Weight'):
            Weights = tf.Variable(tf.random_normal(
                [in_size, out_size]), name='W')
            # random_normal 正态分布生成随机数；
            # random_uniform 平均分布生成随机数，默认值[0,1).
            tf.summary.histogram(layer_name + '/weights', Weights)
        with tf.name_scope('bias'):
            bias = tf.Variable(tf.zeros([1, out_size]) + 0.1)
            tf.summary.histogram(layer_name + '/bias', bias)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + bias
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs


# 训练数据
# x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
# noise = np.random.normal(0, 0.05, x_data.shape)
# y_data = np.square(x_data) - 0.5 + noise
# np.linspace(1,10,10)=[1,2,...,10]
#[1,2,3][:,np.newaxis]=[[1],[2],[3]]
#[1,2,3][np.newaxis,:]=[[1,2,3]]
digits = load_digits()
X = digits.data

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')
# tf.placehoder(tf.float32,shape[行，列])

# 得到输出值
li = add_layer(xs, 1, 10, 0, activation_function=tf.nn.relu)
prediction = add_layer(li, 10, 1, 1)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(
        tf.square(ys - prediction), reduction_indices=[1]))
    tf.summary.scalar('loss', loss)

# with tf.name_scope('loss1'):
#     loss1 = tf.reduce_mean(tf.reduce_sum(
#         tf.square(ys - prediction), reduction_indices=[1]))
#     tf.summary.scalar('loss1', loss1)

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# with tf.name_scope('train1'):
#     train_step1 = tf.train.GradientDescentOptimizer(0.3).minimize(loss1)

# import tensorflow as tf
# a=tf.square([[1],[2],[3]])
# sess=tf.Session()
# b=tf.reduce_mean(a)
# print(sess.run(a))
# print(sess.run(b))

# reduce_sum用法
# a0=tf.reduce_sum([[1,1],[2,2]]) 6
# a1=tf.reduce_sum([[1,1],[2,2]], reduction_indices=0) [3,3]
# a2=tf.reduce_sum([[1,1],[2,2]], reduction_indices=1) [2,4]
# a3=tf.reduce_sum([[1,1],[2,2]], reduction_indices=[1,0]) 6
# a4=tf.reduce_sum([[1,1],[2,2]], reduction_indices=[0,1]) 6
# a5=tf.reduce_sum([[1,1],[2,2]], reduction_indices=[1]) [2,4]

init = tf.global_variables_initializer()
sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('logs1/', sess.graph)
sess.run(init)

# # 画出真实数据图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(x_data, y_data)
# plt.ion()  # 画图延迟暂停
# plt.show()

# 设置一个较大的迭代次数，达到最大迭代次数则认为收敛
for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    #sess.run(train_step1, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        ## print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        # try:
        #     ax.lines.remove(lines[0])
        # except Exception:
        #     pass
        # prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # # 画出预期图像
        # lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        # plt.pause(0.1)
        result = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(result, i)
