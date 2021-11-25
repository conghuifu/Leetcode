import numpy as np
import math

class Neuron:
    # Don't change anything in the `__init__` function.
    def __init__(self, examples):
        np.random.seed(42)
        # Three weights: one for each feature and one more for the bias.
        self.weights = np.random.normal(0, 1, 3 + 1)
        self.num_feature = len(self.weights)
        self.examples = examples
        self.train()

    # Don't use regularization.
    # Use mini-batch gradient descent.
    # Use the sigmoid activation function.
    # Use the defaults for the function arguments.
    def train(self, learning_rate=0.01, batch_size=10, epochs=200):
        # Write your code here.
        for _ in range(epochs):
            for batch_window in range(len(self.examples) // batch_size):
                mini_batch = self.examples[batch_size*batch_window : batch_size + batch_size * batch_window]
                prediction_labels = [
                    {'prediction': self.predict(example['features']),
                     'label': example['label']}
                     for example in mini_batch
                ]
                gradients = self.get_gradients(mini_batch, prediction_labels)
                self.weights -= np.asarray(gradients) * learning_rate

    def get_gradients(self, mini_batch, prediction_labels):
        n = len(mini_batch)
        errors = [prediction['prediction'] - prediction['label'] for prediction in prediction_labels]
        gradients = [0 for i in range(self.num_feature)]
        for example_i, example in enumerate(mini_batch):
            features = example['features'] + [1]
            for feature_i, feature in enumerate(features):
                gradients[feature_i] += errors[example_i]*feature
        gradients = [i/n for i in gradients]
        return gradients

    # Return the probability—not the corresponding 0 or 1 label.
    def predict(self, features):
        # Write your code here.
        features = np.asarray(features + [1])
        wTx = sum(self.weights * features)
        return 1 / (1 + math.exp(-wTx))