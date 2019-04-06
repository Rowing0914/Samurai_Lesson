from keras.optimizers import Adam
from keras import backend as K
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.metrics import categorical_accuracy
import numpy as np

x = K.placeholder(name="x", shape=(None, 28*28))
y_true = K.placeholder(name="y", shape=(None, 10))

W = K.variable(np.random.random((28*28, 10)).astype(np.float32))
b = K.variable(np.random.random((10, )).astype(np.float32))
params = [W, b]

y_pred = K.softmax(K.dot(x, W) + b)
loss = K.mean(K.categorical_crossentropy(y_true, y_pred), axis=None)
accuracy = categorical_accuracy(y_true, y_pred)

opt = Adam()
updates = opt.get_updates(params, [], loss)
train = K.function([x, y_true], [loss, accuracy], updates=updates)

((x_train, y_train), (x_test, y_test)) = mnist.load_data()
x_train = x_train.reshape((-1, 28*28))
y_train = to_categorical(y_train, 10)

for epoch in range(500):
	loss, accuracy = train([x_train, y_train])
	print("Epoch: {}, loss: {}, accuracy: {}".format(epoch, loss, np.mean(accuracy)))
