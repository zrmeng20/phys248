#!/usr/bin/python
'''This is my module
'''

import numpy as np

abc = 123

def mcintmean(func,xrange,N):
    '''MC integration of function func over xrange - mean-value method'''
    Dx = np.diff(xrange)[0]
    x = Dx*np.random.rand(N)+xrange[0]
    favg = func(x).mean()
    I = favg * Dx
    return I

if __name__ == '__main__':    
    func = lambda x: np.sin(1/(x*(2-x)))**2
    print(mcintmean(func,(0,2),100))

