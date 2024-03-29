#%%
import keras
import numpy as np

#%%
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

#%%
def house_model(y_new):
    xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0,7.0], dtype=float)
    ys = np.array([50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0], dtype=float)
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=1000)
    return model.predict(y_new)[0]
#%%
prediction = house_model([7.0])
print(prediction)
#%%
#%%
import keras
import numpy as np

#%%
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

#%%
def house_model(y_new):
    xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0,7.0], dtype=float)
    ys = np.array([50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0], dtype=float)
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=1000)
    return model.predict(y_new)[0]
#%%
prediction = house_model([7.0])
print(prediction)
#%%
