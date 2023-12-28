"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 25/12/2023
"""
from neural_network.layers.neuron import Neuron
from neural_network.layers.hidden_layer import HiddenLayer


class InputLayer:
    def __init__(self, number_of_inputs: 1):
        self.ndims = number_of_inputs
        self.neurons = []
        self.hidden_layer = HiddenLayer()

    def feed_inputs(self, inputs):
        for i in range(self.ndims):
            neuron = Neuron()
            neuron.activation = inputs[i]

            self.neurons.append(neuron)

        #call from main (make each layer independent)
        self.hidden_layer.activate_first_hidden_layer(self.neurons)




