"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 26/12/2023
"""
from typing import List
from neural_network.layers.neuron import Neuron
from neural_network.utils.weights import initialize_weights


class HiddenLayer:
    def __init__(self, no_of_layers: int = 1, neurons_each_layer: int = 1, activation_function: str = ""):
        self.input_layer_neurons: List = []
        self.no_of_layers = no_of_layers
        self.neurons_in_each_layer = neurons_each_layer
        self.weights = None

    def activate_hidden_layer(self, input_layer_neurons: List):
        self.input_layer_neurons.extend(input_layer_neurons)
        input_layer_count = len(self.input_layer_neurons)
        self.weights = initialize_weights(input_layer_count, self.no_of_layers, self.neurons_in_each_layer)

        for i in range(self.no_of_layers):
            pass


