#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

x = np.linspace(0, 50, 1001)
f = lambda x: np.sin(x**0.9)
g = lambda x: np.cos(2*x+np.sqrt(x))
size = [4*i for i in range(39, -1, -1)]
color = np.linspace(39, 0, 40)

def fnc(n):
    plt.scatter(x[n:n+40], f(x)[n:n+40], s=size, c=color, cmap='viridis')
    plt.show()
    fname = f"snake{n}.png"
    plt.savefig("Figs/"+fname, transparent=False)
    
    
def main():
    
    p = Pool(6)
    p.map(fnc, range(0, 960, 1))

if __name__ == '__main__':
    
    main()