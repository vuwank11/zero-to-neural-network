"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 28/12/2023
    Organization: Treeleaf Technologies Pvt. Ltd.
"""
from neural_network.utils.weights import initialize_weights

if __name__ == '__main__':
    weights = initialize_weights(4, 3, 5)
    # should result in 5 (4 rows,3 columns) arrays.

    print(weights)
    print("Shape", weights.shape)