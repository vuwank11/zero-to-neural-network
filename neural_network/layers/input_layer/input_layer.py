"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 25/12/2023
"""
from neural_network.layers.base.neuron import Neuron


class InputLayer:
    def __init__(self, number_of_inputs):
        self.ndims = number_of_inputs
        self.neurons = []

    def feed_inputs(self, inputs):
        for i in range(self.ndims):
            neuron = Neuron()
            neuron.activation = inputs[i]

            self.neurons.append(neuron)

    def activate_first_hidden_layer(self):
        pass


