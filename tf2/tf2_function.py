import tensorflow as tf
class TFFunction:
    def __init__(self):
        pass

    def execute(self):
        mnist = tf.keras.datasets.mnist
        (x_train,y_train),(x_test,y_test) = mnist.load_data()
        x_train,x_train = x_train/255.0,x_test/255.0
        # 채널차원 추가
        x_train = x_train[...,tf.newaxis]
        x_test = x_test[...,tf.newaxis]
        train_ds = tf.data.Dataset.from_tensor_slices(
            (x_train,y_train)
        ).shuffle(10000).batch(32)
        test_ds = tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(32)
        print(test_ds)
if __name__ == '__main__':
    t = TFFunction()
    t.execute()