'''This is my module
'''

from multiprocessing import Pool
import numpy as np

eps = 1.e-5
def mcintmean(func,xrange=[eps,2-eps],N=1000):
    '''MC integration of function func over xrange - mean-value method'''
    Dx = np.diff(xrange)[0]
    x = Dx*np.random.rand(N)+xrange[0]
    favg = func(x).mean()
    I = favg * Dx
    return I

func = lambda x: np.sin(1/(x*(2-x)))**2

def m_(i):
    return mcintmean(func)

p = Pool(4)
#print(p.map(m_, range(100000)))
mcs = np.array(p.map(m_, range(100000)))
print(f"Mean = {mcs.mean():9.4f}, sigma = {mcs.std():9.4f}")
