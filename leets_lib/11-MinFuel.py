def minFuel(x, y):

    n = len(x)
    x.sort()
    for i in range(n):
        x[i] -= i
    y.sort()
    x.sort()
    
    fuel = 0
    for i in range(n):
        fuel += abs(y[i] - y[n//2])
        fuel += abs(x[i] - x[n//2])

    return fuel
