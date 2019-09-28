import tensorflow as tf
import numpy as np

class SeqModel:
    def __init__(self):
        self.model = None
    @staticmethod
    @tf.function
    def simple_func():
        a = tf.constant(1)
        b = tf.constant(2)
        c = tf.constant(3)
        z = a + b + c
        return z