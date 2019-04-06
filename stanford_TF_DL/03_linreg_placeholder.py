import time
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import utils

DATA_FILE = 'data/birth_life_2010.txt'
data, n_samples = utils.read_birth_life_data(DATA_FILE)
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')
w = tf.get_variable('weights', initializer=tf.constant(0.0))
b = tf.get_variable('bias', initializer=tf.constant(0.0))
Y_predicted = w * X + b
loss = tf.square(Y - Y_predicted, name='loss')
optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=0.001).minimize(loss)
start = time.time()
writer = tf.summary.FileWriter('./graphs/linear_reg', tf.get_default_graph())
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(100):
        total_loss = 0
        for x, y in data:
            _, l = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss/n_samples))
    writer.close()

    w_out, b_out = sess.run([w, b])

plt.plot(data[:, 0], data[:, 1], 'bo', label='Real Data')
plt.plot(data[:, 0], data[:, 0]*w_out+b_out, 'r', label='Prediction')
plt.legend()
plt.show()
