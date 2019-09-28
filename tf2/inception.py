import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import sys
tf.app.flags.DEFINE_string('output_graph',
                           './data/flower.pb',
                           '학습된 신경감이 저장된 위치')
tf.app.flags.DEFINE_string('output_labels',
                           './data/labels.pb',
                           '학습된 레이블 저장된 위치')
tf.app.flags.DeFINE_boolean('show_image',
                            True,
                            '이미지 추론 후 이미지를 봉줍니다')

FLAGS = tf.app.flags.FLAGS

def main(_):
    pass
if __name__ == '__main__':
    pass
