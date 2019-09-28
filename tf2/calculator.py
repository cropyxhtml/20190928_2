import tensorflow as tf
import numpy as np
class Add:
    def __init__(self,a=0,b=0):
        pass
    def execute(self,a,b):
        return tf.constant(a) + tf.constant(b)
class Mean:
    def __init__(self):
        pass
    def execute(self,a,b):
        x_array = np.arange(18).reshape(3,2,2)
        x2 = tf.reshape(x_array, shape=(-1,6))
        # 각 열의 합을 계산
        xsum = tf.reduce_sum(x2, axis=0)
        # 각 열의 평균을 계산
        xmean = tf.reduce_mean(x2, axis=0)

        print('입력 크기 :',x_array.shape)
        print('크기가 변형된 입력 크기 :\n',x2.np())
        print('열의 합:\n', xsum.np())
        print('열의 평균:\n', xmean.np())

if __name__ == '__main__':
    print('입력')
    menu = int(input('하세요:'))
    if menu == 1:
        m = Add()
        print(m.execute(5,7))
    elif menu ==2:
        m = Mean()
        print(m.execute())
