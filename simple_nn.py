import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generate some dummy data
# Features (X): 100 samples, each with 2 features
# Labels (y): Binary classification (0 or 1)
np.random.seed(42)
X = np.random.rand(100, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Label is 1 if the sum of features > 1

# Define the neural network
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),  # Hidden layer with 4 neurons
    Dense(1, activation='sigmoid')                 # Output layer with 1 neuron
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=50, batch_size=10, verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(X, y, verbose=0)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

# Make predictions
predictions = model.predict(X[:5])
print("Predictions for the first 5 samples:")
print(predictions)