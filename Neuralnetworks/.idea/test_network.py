import numpy as np
import network as nw
import mnist_loader as mnist_l
import CNN as cnn
import network3

#training_data,validation_data,test_data=mnist_l.load_data_wrapper()
#net=nw.Network([784,30,10])
#net.SGD(training_data,30,10,3.0,test_data=test_data)
#training_data, validation_data, test_data = network3.load_data_shared()
net=cnn.regularized_dbl_conv()