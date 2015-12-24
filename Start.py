from Gameoflife import *
from Matrix import *
from Testlibrary import *
import sys
import time
import numpy
import os
os.system('clear')
print "Welcome to Game of Life"

# test cases
if len(sys.argv) > 1 and sys.argv[1] == "test":
    TestCaseOne()
    TestExploder()
else:  # speed testing
    x = initMatrix()
    print x
    print "number of ones", numpy.count_nonzero(x)
    start = time.clock()
    for i in range(10000):
        gameoflife(x)
        os.system('clear')
        print x
        time.sleep(0.8)

    end = time.clock()
    time = end-start
    print "Passed Time ", time, "s"
