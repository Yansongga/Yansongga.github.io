#m = 4### number of edges
n = 4 ### number of nodes
a, b, c = 0, 2, 1  ### home building, office

from_ = [0, 1, 0, 1]
to_ = [1, 2, 3, 3]
weight = [ 2, 6, 3, 1]
import collections
def min_path( n, a, b, c, from_, to_, weight):
    
    m = len(from_)
    q = collections.deque()
    
    ad = {}
    e_map = {}
    for idx in range(m):
        i, j = from_[idx], to_[idx]
        e_map[ (i, j) ] = idx
        e_map[ (j, i) ] = idx
        ad.setdefault( i, [])
        ad.setdefault( j, [])
        ad[i].append(j)
        ad[j].append(i)
        
    if a == b and b == c:
        return 0 
     ## state variable ( node, build, office, seen_road, cost)
     
    if a == b:
        build = True
    else:
        build = False
        
    curr = ( a, build, 0, 0 )
    q.append( (a, build, 0, 0 ) )
    memo = set()
    memo.add( curr )
    
    out = float('inf')
    while q:
        (node, build, seen, cost) = q.popleft()
        
        if build == True and node == c:
            out = min( out, cost )
            continue
        
        for next_ in ad[node]:
            e_id = e_map[ node, next_ ]
            seen_next = seen | (2 ** e_id)
            
            ## update seen/ cost
            if seen_next != seen:
                cost_next = cost + weight[e_id]
            else:
                cost_next = cost
            
            ## update build
            if node == b:
                build_next = True
            else:
                build_next = build
                
            if (next_, build_next, seen_next, cost_next) not in memo:
                memo.add( (next_, build_next, seen_next, cost_next) )
                q.append( (next_, build_next, seen_next, cost_next) )
                
    
    if out < float('inf'):
        return out
    else:
        return -1
        

print(min_path( n, a, b, c, from_, to_, weight) )
