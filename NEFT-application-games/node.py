import math

class Node:
    def __init__(self, id_number):
        self.id_number = id_number
        self.layer = 0
        self.input_value = 0
        self.ouput_value = 0
        self.connections = []

    def activate(self):
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))
        
        if self.layer == 1:
            self.ouput_value = sigmoid(self.input_value)
        
        for i in range(0, len(self.connections)):
            self.connections[i].dst.input_value += self.connections[i].weight * self.ouput_value
        
        