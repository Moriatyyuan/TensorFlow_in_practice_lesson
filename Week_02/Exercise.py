#%%
import tensorflow as tf
import keras


#%%
class MyCallbacks(tf.keras.callbacks.Callback):
    def om_epoch_end(self, epoch, logs={}):
        if logs.get("acc") > 0.99:
            print("\nReached 60% accuracy so cancelling training!")
            self.model.stop_training = True


# GRADED FUNCTION: train_mnist
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    # YOUR CODE SHOULD START HERE
    callbacks = MyCallbacks()
    # YOUR CODE SHOULD END HERE

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # YOUR CODE SHOULD START HERE
    x_train = x_train / 255.0
    x_test = x_test / 255.0
    # YOUR CODE SHOULD END HERE
    model = tf.keras.models.Sequential(
        [
            keras.layers.Flatten(input_shape=[28, 28]),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(10, activation=tf.nn.softmax),
        ]
    )

    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )

    # model fitting
    history = model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
    # model fitting
    return history.epoch, history.history["acc"][-1]


#%%
train_mnist()


#%%
