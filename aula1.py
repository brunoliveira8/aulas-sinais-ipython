# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:55:33 2015
@author: bruno
"""

import numpy as np
from pylab import *

#define the delta function
def dd1(n):
    if n:
        return 0
    return 1

#define the step function
def step(n):
    if n < 0:
        return 0
    return 1
    
#define the number of samples
n = np.arange(-5,5)

#declare a vector with 10 spaces but empty values
impseq = np.empty((len(n),), dtype = int)

#define the values of impseq
for i in range(len(n)):
    impseq[i] = dd1(n[i])


#plot the stick grapph
figure(1)
markerline, stemlines, baseline = stem(n,impseq,linefmt='b')
axis([-5,4,-2,2])
grid()
setp(stemlines, 'linewidth','2.0')
xlabel('n')
ylabel('x[n]=u[n-n0]')
title('Step Sequence Response')


#declare a vector with 10 spaces but empty values
stepseq = np.empty((len(n),), dtype = int)


#define the values of impseq
for i in range(len(n)):
    stepseq[i] = step(n[i])

#plot the stick grapph
figure(2)
markerline, stemlines, baseline = stem(n,impseq,linefmt='b')
axis([-5,4,-2,2])
grid()
setp(stemlines, 'linewidth','2.0')
xlabel('n')
ylabel('x[n]=u[n-n0]')
title('Step Sequence Response')


conv = np.convolve(stepseq, stepseq)
nconv =np.arange(-len(n),len(n)-1)

#plot the stick grapph
figure(3)
markerline, stemlines, baseline = stem(nconv,conv,linefmt='b')
axis([-10,10,-2,6])
grid()
setp(stemlines, 'linewidth','2.0')
xlabel('n')
ylabel('x[n]=u[n-n0]')
title('Step Sequence Response')