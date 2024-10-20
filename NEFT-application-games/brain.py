import node
import connection
import random


class Brain:
    def __init__(self, inputs, clone = False):
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.graph = []
        self.layers = 2

        if not clone:
            # Create input nodes
            for i in range(0, self.inputs):
                self.nodes.append(node.Node(i))
                self.nodes[i].layer = 0

            # Create bias node
            self.nodes.append(node.Node(3))
            self.nodes[3].layer = 0

            # Create output layer
            self.nodes.append(node.Node(4))
            self.nodes[4].layer = 1
            
            # Create connections
            for i in range(0, 4):
                self.connections.append(connection.Connection(self.nodes[i], self.nodes[4], random.uniform(-1, 1)))

    def conncet_nodes(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i].connections = []

        for i in range (0, len(self.connections)):
            self.connections[i].src.connections.append(self.connections[i])
    
    def generate_graph(self):
        self.conncet_nodes()
        self.graph = []

        for i in range(0, self.layers):
           for j in range(0, len(self.nodes)):
               if self.nodes[j].layer == i:
                   self.graph.append(self.nodes[j])
    
    def feed_forward(self, vision):
        for i in range(0, self.inputs):
            self.nodes[i].output_value = vision[i]
            #print(vision[i])

        self.nodes[3].output_value = 1

        for i in range(0, len(self.graph)):
            self.graph[i].activate()
        
        output_value = self.nodes[4].output_value

        for i in range(0, len(self.nodes)):
            self.nodes[i].input_value = 0
        
        return output_value
    
    def clone(self):
        clone = Brain(self.inputs, True)

        for n in self.nodes:
            clone.nodes.append(n.clone())
        
        for c in self.connections:
            clone.connections.append(c.clone(clone.getNode(c.src.id), 
                                             clone.getNode(c.dst.id)))
        
        clone.layers = self.layers
        clone.conncet_nodes()
        return clone
    
    def getNode(self, id):
        return self.nodes[id]

    def mutate(self):
        if random.uniform(0, 1) < 0.8:
            for i in range(0, len(self.connections)):
                self.connections[i].mutate_weight()

