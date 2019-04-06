import tensorflow as tf

c = tf.random_uniform([], -10, 10, seed=2)
with tf.Session() as sess:
    print(sess.run(c))
    print(sess.run(c))

c = tf.random_uniform([], -10, 10, seed=2)
with tf.Session() as sess:
    print(sess.run(c))
    print(sess.run(c))

with tf.Session() as sess:
    print(sess.run(c))
    print(sess.run(c))

c = tf.random_uniform([], -10, 10)