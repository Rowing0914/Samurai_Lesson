import numpy as np
import tensorflow as tf
import utils

learning_rate = 0.01
batch_size = 128
n_epochs = 30
n_train = 60000
n_test = 10000

mnist_folder = 'data/mnist'
utils.download_mnist(mnist_folder)
train, val, test = utils.read_mnist(mnist_folder, flatten=True)

train_data = tf.data.Dataset.from_tensor_slices(train)
train_data = train_data.shuffle(10000)
train_data = train_data.batch(batch_size)

test_data = tf.data.Dataset.from_tensor_slices(test)
test_data = test_data.batch(batch_size)

iterator = tf.data.Iterator.from_structure(train_data.output_types,
                                           train_data.output_shapes)
img, label = iterator.get_next()

train_init = iterator.make_initializer(train_data)
test_init = iterator.make_initializer(test_data)

w = tf.get_variable(name='weights', shape=(784, 10),
                    initializer=tf.random_normal_initializer(0, 0.01))
b = tf.get_variable(name='bias', shape=(
    1, 10), initializer=tf.zeros_initializer())

logits = tf.matmul(img, w) + b
entropy = tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=label, name='entropy')
loss = tf.reduce_mean(entropy, name='loss')
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

preds = tf.nn.softmax(logits)
correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(label, 1))
accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))

writer = tf.summary.FileWriter('./graphs/logreg', tf.get_default_graph())
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(n_epochs):
        sess.run(train_init)
        total_loss = 0
        n_batches = 0
        try:
            while True:
                _, l = sess.run([optimizer, loss])
                total_loss += l
                n_batches += 1
        except tf.errors.OutOfRangeError:
            pass
        print('Average loss epoch {0}: {1}'.format(i, total_loss/n_batches))
        sess.run(test_init)
        total_correct_preds = 0

        try:
            while True:
                accuracy_batch = sess.run(accuracy)
                total_correct_preds += accuracy_batch
        except tf.errors.OutOfRangeError:
            pass
        print('Accuracy {}'.format(total_correct_preds/n_test))
    writer.close()
