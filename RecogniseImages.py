import ImageLoader
import NeuralNet

training_data, validation_data, test_data = ImageLoader.load_data_wrapper()

net = NeuralNet.Network([784, 300,20, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

