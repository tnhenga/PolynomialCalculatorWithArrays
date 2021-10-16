import numpy as np


def f(x, coef):
    
    x = np.array(x, dtype=float)
    print('Array size of x:', x.size)

    coef = np.array(coef, dtype=float)
    print('Array size of coef:', coef.size)
    
    result = np.inner(x, coef)
    print('Array multiplication:', result)
    
    result = coef[0] + ( coef[1]*x**1 ) + (coef[2]*x**2)
    #result = sum(result) + ((x-1)**2)
    
    return result

print( f(2.0, [1,2,1]) )