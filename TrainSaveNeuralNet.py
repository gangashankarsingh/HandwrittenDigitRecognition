import ImageLoader
import NeuralNet
import datetime
import pickle as cPickle

a = str(datetime.datetime.now()).split()
filepath  = "./SavedModels/"

filename = "Model" + a[0]+"_"+a[1]


training_data, validation_data, test_data = ImageLoader.load_data_wrapper()

net = NeuralNet.Network([784, 40, 10])
net.SGD(training_data, 40, 10, 3.0, test_data=test_data)

filename = str(net.accuracy) + "::" + filename

filehandler = open(filepath+filename, 'wb')

cPickle.dump(net, filehandler)

