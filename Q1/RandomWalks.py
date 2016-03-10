###########################################
# Section 2
###########################################
import random
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values


ep = [1, -1];
def nextEp():
    return random.choice(ep)


"""
Recursively make path
"""
def path(i):
    if( i == 0 ):
        return [nextEp()]
    else:
        xi = path(i-1)
        xi.append(nextEp())
        return xi

def xSum(path):
    return sum(path)

def mean(path):
    return sum(path)/float(len(path))

def var(path):
    avg = mean(path)
    return sum(((val - avg)**2 ) for val in path)/len(path)


#Test that stuff

means  = [] 
varis  = []
xs = []
for T in range(10,4000,10):
    p = path(T)
    means.append(mean(p))
    varis.append(var(p))
    xs.append(xSum(p))

print "Average mean: "+str(mean(means))
print "Average Var:  "+str(mean(varis))

data = [
    go.Histogram(x=xs)
]

plotly.offline.plot(data, filename="Random Walk Histogram");

