import math

def n_distro(x,m,s):
    '''Enter the corresponding value, s.d and mean'''
    v1=float(1/(math.sqrt(2*math.pi)*s))
    v2=math.exp(-(0.5)*math.pow(((x-m)/s),2))
    prob=v1*v2
    return prob

def mean(mn):
    sm=0
    for i in mn:
        sm+=i
    mean=sm/len(mn)
    return mean

def sd(mn,mean):
    summer=0
    for i in range(0,len(mn)):
        summer+=math.pow(mn[i]-mean,2)
    summer/=len(mn)
    return(math.sqrt(summer))

