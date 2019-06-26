import numpy as np

class Helpers:
    def __init__(self):
        pass

    @staticmethod
    def convert_array_strings_to_ints(input):
        return np.array([int(y) for y in input])