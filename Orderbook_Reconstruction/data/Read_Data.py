import numpy



x = numpy.load('update_order_btcusd.npy')
numpy.set_printoptions(suppress=True)
first = x[0][4]
last = x[x.shape[0]-1][4]
print(first, last)
y = x[0]
print(y)
