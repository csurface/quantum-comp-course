import math
import matplotlib.pyplot as mpl
import numpy as np

# Modular arithmetic to find prime factors of a number N

N = 15
a = 13

print(math.gcd(a, N))

z = list(range(N))
y = [a**z0 % N for z0 in z]

print(z)
print(y)

mpl.plot(z,y)
mpl.xlabel('z')
mpl.ylabel('{}^z (mod {})'.format(a,N))
mpl.show()

# the period is 4 (how often the graph repeats itself)
r = z[y[1:].index(1)+1]
print(r)

if r % 2 == 0:
    # period is an even number
    x = (a**(r/2.)) % N
    print('x: {}'.format(x))
    if ((x+1) % N) != 0:
        print(math.gcd((int(x)+1),N), math.gcd((int(x)-1),N))
    else:
        print('x+1 is 0 (mod N)')
else:
    print('r is odd')
