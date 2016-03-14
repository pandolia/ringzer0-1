# -*- coding:utf-8 -*-

import math

if __name__ == '__main__':
    total = 0
    for index in range(500):
        print "index {}: current: {}".format(index,int(math.pow(6,index)))
        total += int(math.pow(6,index))
        print total

    print total
