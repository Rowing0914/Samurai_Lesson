import tensorflow as tf
tf.enable_eager_execution()

n = 10
x = tf.random_normal([n, 2])
noise = tf.random_normal([n, 2])

y = x * 3 + 2 + noise

class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.dense1 = tf.keras.layers.Dense(units = 1, activation='relu')
    def call(self, inputs):
        return self.dense1(x)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

model = Model()
with tf.GradientTape() as tape:
  error = model(x) - y  # NOT model.predict(x) - y
  loss_value = tf.reduce_mean(tf.square(error))
gradients = tape.gradient(loss_value, model.variables)
print(gradients)
optimizer.apply_gradients(zip(gradients, model.variables),
                            global_step=tf.train.get_or_create_global_step())