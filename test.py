"""This is a test.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import numpy as np
import theano
import theano.tensor as T

x = T.dmatrix("x")
y = T.dmatrix("y")
print "something is working"
y = 2*x

fun = theano.function([x], y)

print fun(np.asarray([[1, 2, 3], [4, 5, 6]]))

for i in xrange(10):
    print i
    print i
