import numpy as np
import tensorflow as tf

a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
x = tf.add(a, b, name='add')

writer = tf.summary.FileWriter('./graphs/simple', tf.get_default_graph())

with tf.Session() as sess:
    print(sess.run(x))
writer.close()

a = tf.constant([2, 2], name='a')
b = tf.constant([[0, 1], [2, 3]], name='b')

with tf.Session() as sess:
    print(sess.run(tf.div(b, a)))
    print(sess.run(tf.divide(b, a)))
    print(sess.run(tf.truediv(b, a)))
    print(sess.run(tf.floordiv(b, a)))
    print(sess.run(tf.truncatediv(b, a)))
    print(sess.run(tf.floor_div(b, a)))

a = tf.constant([10, 20], name='a')
b = tf.constant([2, 3], name='b')

with tf.Session() as sess:
    print(sess.run(tf.multiply(a, b)))
    print(sess.run(tf.tensordot(a, b, 1)))

t_0 = 19
x = tf.zeros_like(t_0)
y = tf.zeros_like(t_0)

t_1 = ['apple', 'peach', 'banana']
x = tf.zeros_like(t_1)

my_const = tf.constant([1.0, 2.0], name='my_const')
print(tf.get_default_graph().as_graph_def())
