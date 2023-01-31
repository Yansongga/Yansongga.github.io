a = 2
b = 3
c = 5
n = 100

def bitsolver(a, b, c, n):
    seq = [a, b, c]
    if n < 3:
        return seq[n]
        
    a_, b_, c_ = a, b, c
    for idx in range(3, n):
        f_n = (a_ | b_) ^ c_
        seq.append( f_n )
        a_ = b_
        b_ = c_
        c_ = f_n
        
    return seq
    
print(bitsolver(a, b, c, n))
