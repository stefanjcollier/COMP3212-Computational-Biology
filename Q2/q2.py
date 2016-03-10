from math import exp
from math import log
from math import factorial
from random import random
import plotly
import plotly.plotly as py
import plotly.graph_objs as go



def p(x, u):
    return u * exp(-u,x)

def b_a(a, mu):
    if (a == 1.0):
        return 0
    return -1.0/mu * log(1-a)

def b(mu):
    return b_a(random(),mu)

def pois(k,lam):
    return lam**k * exp(-lam) / factorial(k)



def b_events(T,mu):
    total = 0.0
    events = 0
    while(True):
        total += b(mu)
        if(total > T):
            return events
        else:
            events+= 1

def pois_events(events, T,lam):
    k = int(round(events,0))/T
    return pois(k,lam)

T = 10
mu = 4  

avg = 0.0
tests= 10000
xs = []
for i in range(0,tests):
    res = b_events(T,mu)
    avg += res
    xs.append(res)

avg /= tests

#This is the number of events per T calc'd by using 'b's
print str(int(round(avg)))+" events occurred in "+str(T)+" time units"
data = [
    go.Histogram(x=xs)
    ]
plotly.offline.plot(data, filename="Events occuring");

#Using delta_t = 1 
lam1 = mu
lam2 = 1.0/mu
lam3 = mu*mu
lam4 = exp(mu)
lam5 = log(mu)

print pois_events(avg,T, lam1)
print pois_events(avg,T, lam2)
print pois_events(avg,T, lam3)
print pois_events(avg,T, lam4)
print pois_events(avg,T, lam5)







