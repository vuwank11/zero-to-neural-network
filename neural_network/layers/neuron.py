"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 24/12/2023
"""
from neural_network.utils.activations import get_activation_func


class Neuron(object):
    def __init__(self, activation: float = 0.0, activation_func: str = "", bias: float = 0.0):
        self.activation = activation
        self.activation_function = get_activation_func(activation_func)
        self.bias = bias
