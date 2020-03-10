import math
import numpy as np
from numpy import linalg

# Just some Equations
r1 = 1
r2 = 1
r3 = 1
alpha1 = 1
alpha2 = 1
alpha3 = 1
zeta1 = 1
zeta2 = 1
zeta3 = 1

c1 = r3*math.cos(alpha2 + zeta3) - r2*math.cos(alpha3 + zeta2)
c2 = r3*math.sin(alpha2 + zeta3) - r2*math.sin(alpha3 + zeta2)
c3 = r1*math.cos(alpha3 + zeta1) - r3*math.cos(zeta3)
c4 = -r1*math.sin(alpha3 + zeta1) + r3*math.sin(zeta3)
c5 = r1*math.cos(alpha2 + zeta1) - r2*math.cos(zeta2)
c6 = -r1*math.sin(alpha2 + zeta1) + r2*math.sin(zeta2)

a1 = -c3**2 - c4**2
a2 = c3*c6 - c4*c5
a3 = -c4*c6 - c3*c5
a4 = c2*c3 + c1*c4
a5 = c4*c5 - c3*c6
a6 = c1*c3 - c2*c4

k1 = a2*a4 + a3*a6
k2 = a3*a4 + a5*a6
k3 = (a1**2 - a2**2 - a3**3 - a4**4 - a6**2)/2

# TODO: exception handling
# simply compare the betas against alphas and take the unique beta
beta31 = 2*math.atan((k2+math.sqrt(k1**2 + k2**2 -k3**2))/(k1 + k3))
beta32 = 2*math.atan((k2-math.sqrt(k1**2 + k2**2 -k3**2))/(k1 + k3))

beta2 = math.atan( -(a3*math.sin(beta3) + a2*math.cos(beta3) + a4)/
                   -(a5*math.sin(beta3) + a3*math.cos(beta3) + a6))


# step 2
w1X = w*math.cos(theta)
w1Y = w*math.sin(theta)
z1X = z*math.cos(phi)
z1Y = z*math.sin(phi)

np.