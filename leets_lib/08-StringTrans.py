# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# A = AvoidSet
# 0 < t1, t2,..., tk < n
### Two cases, if 0 \notin A, then 0 \in A_bar
### t1 has n - |A| - 1 choices, 
### for 1 <i < k, s(i-1) \in A_bar and 
## s(i -1) + ti \in \bar{A}, ti \ in  \bar{A} - s(i -1)
### ti has  | \abr{A} | - 1 = n - |A| - 1 choices

### if 0 \in A, 
### t1 has n-|A| choices, and. 0 \notin \bar{A}

### s_{i-1} \in \bar{A}, and
### s_{i-1} + t_i \in \bar{A,
### t_i has n-1-|A| choices
src = 'abab'
target = 'abab'
k =3
def trans(src, target, k):
    ## compute the avoid set
    avoid = []
    if len(src) != len(target):
        return 0
    if k == 0:
        return 0 
    n = len(src)
    for a in range( n ):
        if a == 0:
            new_s = src
        else:
            new_s = src[n-a :] + src[:n-a]
            
        if new_s == target:
            avoid.append( a )
    num_a = len( avoid )        
    if 0 in avoid:
        if k ==1:
            return num_a -1
        return ( n - num_a ) * ( (n - num_a - 1)**(k-2) ) * num_a
        
    elif 0 not in avoid:
        if k ==1:
            return num_a
        return ( (n - num_a - 1)**(k-1) ) * num_a
        
print( trans(src, target, k) )
