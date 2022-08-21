from typing import Optional


class Layer:
    name = 'Layer'
    next_layer: 'Optional[Layer]' = None

    def __call__(self, layer: 'Layer'):
        self.next_layer = layer
        return layer


class Input(Layer):
    name = 'Input'
    inputs: int

    def __init__(self, inputs: int):
        self.inputs = inputs


class Dense(Layer):
    name = 'Dense'
    inputs: int
    outputs: int
    activation: str

    def __init__(self, inputs: int, outputs: int, activation: str):
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    network: Layer

    def __init__(self, network: Layer):
        self.network = network

    def __iter__(self):
        current = self.network
        while current:
            yield current
            current = current.next_layer



