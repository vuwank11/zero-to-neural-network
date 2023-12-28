"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 26/12/2023
"""
import numpy as np


def initialize_weights(previous_layer_count, neurons_in_each_layer: int = 1,  no_of_layers: int = 1):
    """
    :param previous_layer_count: no. of neurons in the previous layer.
    :param no_of_layers: no. of layers in hidden layer(default 1 for output layer)
    :param neurons_in_each_layer: no. of neurons in each layer.
    :return: weight array of shape (no_of _layer, previous_layer_count, neurons_in_each_layer).
    """

    # Outermost dimension is written first followed by the inner dimensions.
    weights = np.random.rand(no_of_layers, previous_layer_count, neurons_in_each_layer)

    return weights


