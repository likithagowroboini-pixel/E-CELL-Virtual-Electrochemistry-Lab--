import math

R = 8.314462618
F = 96485.33212

def ecell(ecathode, eanode):
    return ecathode - eanode

def nernst(E0, n, Q, T):
    return E0 - (R*T/(n*F))*math.log(Q)

def gibbs(n, E):
    return -n*F*E
