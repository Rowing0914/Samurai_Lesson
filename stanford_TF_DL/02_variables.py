import tensorflow as tf
import numpy as np

s = tf.Variable(2, name='scalar')
m = tf.Variable([[0, 1], [2, 4]], name='matrix')
w = tf.Variable(tf.zerors([784, 10]), name='big_matrix')
v = tf.Variable(tf.truncated_normal([784, 10]), name='normal_matrix')
s = tf.get_variable('scalar', initializer=tf.constant(2))
m = tf.get_variable('matrix', initializer=tf.constant([[0, 1], [2, 3]]))
w = tf.get_variable('big_matrix', shape=(784, 10),
                    initializer=tf.zeros_initializer())
v = tf.get_variable('normal_matrix', shape=(784, 10),
                    initializer=tf.truncated_normal_initializer())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(v.eval())

w = tf.Variable(10)
w.assign(100)

with tf.Session() as sess:
    sess.run(w.initializer)
    print(sess.run(w))

w = tf.Variable(10)
assign_op = w.assign(100)
with tf.Session() as sess:
    sess.run(assign_op)
    print(w.eval())

a = tf.get_variable('scalar', initializer=tf.constant(2))
a_times_two = a.assign(a*2)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(a_times_two)
    sess.run(a_times_two)
    sess.run(a_times_two)

w = tf.Variable(10)
with tf.Session() as sess:
    sess.run(w.initializer)
    print(sess.run(w.assign_add(10)))
    print(sess.run(w.assign_sub(2)))

w = tf.Variable(10)
sess1 = tf.Session()
sess2 = tf.Session()
sess1.run(w.initializer)
sess2.run(w.initializer)
print(sess1.run(w.assign_add(10)))
sess1.close()
sess2.close()
