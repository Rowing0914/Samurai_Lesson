import tensorflow as tf
import tensorflow.contrib.eager as tfe
import matplotlib.pyplot as plt
import utils

DATA_FILE = 'data/birth_life_2010.txt'
tfe.enable_eager_execution()
data, n_samples = utils.read_birth_life_data(DATA_FILE)
dataset = tf.data.Dataset.from_tensor_slices((data[:,0], data[:,1]))

w = tfe.Variable(0.0)
b = tfe.Variable(0.0)

def prediction(x):
    return x*w + b

def squared_loss(y, y_pred):
    return (y - y_pred)**2

def huber_loss(y, y_pred, m=1.0):
    """ Huber loss """
    t = y - y_pred
    return t**2 if tf.abs(t) <= m else m*(2*tf.abs(t)-m)

def train(loss_fn):
    """ Train a regression model evaluated using `loss-fn` """
    print("Training: loss function: " + loss_fn.__name__)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    
    def loss_for_example(x, y):
        return loss_fn(y, prediction(x))

    grad_fn = tfe.implicit_value_and_gradients(loss_for_example)

    for epoch in range(100):
        total_loss = 0.0
        for x_i, y_i in tfe.Iterator(dataset):
            loss, gradients = grad_fn(x_i, y_i)
            optimizer.apply_gradients(gradients)
            total_loss += loss
        if epoch % 10 == 0:
            print('Epoch {0}: {1}'.format(epoch, total_loss/n_samples))

train(huber_loss)
plt.plot(data[:,0], data[:,1], 'bo')
plt.plot(data[:,0], data[:,0]*w.numpy() + b.numpy(), 'r')
plt.show()