import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import utils

learning_rate = 0.01
batch_size = 128
n_epochs = 30

mnist = input_data.read_data_sets('data/mnist', one_hot=True)
X_batch, Y_batch = mnist.train.next_batch(batch_size)

X = tf.placeholder(tf.float32, [batch_size, 784], name='image')
Y = tf.placeholder(tf.int32, [batch_size, 10], name='label')

w = tf.get_variable(name='weights', shape=(784, 10),
                    initializer=tf.random_normal_initializer())
b = tf.get_variable(name='bias', shape=(
    1, 10), initializer=tf.zeros_initializer())

logits = tf.matmul(X, w) + b
entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=logits, labels=Y, name='loss')
loss = tf.reduce_mean(entropy)

optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

preds = tf.nn.softmax(logits)
correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))

writer = tf.summary.FileWriter(
    './graphs/logreg_placeholder', tf.get_default_graph())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    n_batches = int(mnist.train.num_examples/batch_size)
    for i in range(n_epochs):
        total_loss = 0
        for j in range(n_batches):
            X_batch, Y_batch = mnist.train.next_batch(batch_size)
            _, l = sess.run([optimizer, loss], {X: X_batch, Y: Y_batch})
            total_loss += l
        print('Average loss epoch {0}: {1}'.format(i, total_loss/n_batches))
    n_batches = int(mnist.test.num_examples/batch_size)
    total_correct_preds = 0

    for i in range(n_batches):
        X_batch, Y_batch = mnist.test.next_batch(batch_size)
        accuracy_batch = sess.run(accuracy, {X: X_batch, Y: Y_batch})
        total_correct_preds += accuracy_batch
    print('Accuracy {}'.format(total_correct_preds/mnist.test.num_examples))
