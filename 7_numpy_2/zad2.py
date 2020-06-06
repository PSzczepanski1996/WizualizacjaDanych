import numpy

a = numpy.arange(9).reshape((3, 3))
b = numpy.arange(16).reshape((4, 4))
print(numpy.amin(a, 1), numpy.amin(b, 1))