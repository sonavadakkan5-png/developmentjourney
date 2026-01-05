def emi(P,R,N):

    return (P * R * (1 + R)**N) / ((1 + R)**N - 1)

print(round(emi(10000,2,3)))