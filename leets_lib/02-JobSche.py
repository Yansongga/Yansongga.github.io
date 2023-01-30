# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
m = 17### number of jobs
n = 5 ### number of workers
k = 3 #### index of the best worker

def max_k(m, n, k):
    
    m -= n
    def sum_( peak ):
        left = max( peak - k, 0 )
        out = int( ( left + peak ) * ( peak - left +1 ) /2 )
        right = max( peak - (n-1 - k), 0 )
        out += int((right + peak) * ( peak -right +1) /2)
        return out - peak
        
    left, right = 0, m
    while right > left :
        
        mid = ( left + right + 1 ) // 2
        #print( left, right, mid, sum_( mid ), m )
        if sum_( mid ) > m:
            right = mid - 1
        else:
            left = mid 
            
    return right +1
    
print( max_k(m, n, k) )
