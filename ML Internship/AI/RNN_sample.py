#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate the Sine Wave dataset
def generate_sine_wave_data(num_samples, sequence_length):
    time_steps = np.linspace(0, 10, num_samples)
    data = np.sin(time_steps)
    x = []
    y = []
    for i in range(len(data) - sequence_length):
        x.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(x), np.array(y)

# RNN parameters
sequence_length = 10
input_size = 1
hidden_units = 32
output_size = 1

# Generate the dataset
num_samples = 1000
x_train, y_train = generate_sine_wave_data(num_samples, sequence_length)

# Reshape the input data to fit the RNN model (batch size, sequence length, input size)
x_train = x_train.reshape(-1, sequence_length, input_size)

# Build the RNN model
model = tf.keras.Sequential([
    tf.keras.layers.SimpleRNN(hidden_units, input_shape=(sequence_length, input_size)),
    tf.keras.layers.Dense(output_size)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the RNN
model.fit(x_train, y_train, epochs=50, batch_size=32)

# Predict using the trained RNN
x_test, y_test = generate_sine_wave_data(20, sequence_length)
x_test = x_test.reshape(-1, sequence_length, input_size)
predictions = model.predict(x_test)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(np.arange(sequence_length, sequence_length + len(predictions)), y_test, label='True Values')
plt.plot(np.arange(sequence_length, sequence_length + len(predictions)), predictions, label='Predictions')
plt.xlabel('Time Steps')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[ ]:




