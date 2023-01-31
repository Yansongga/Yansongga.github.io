from_ = [0, 0, 1, 0, 3 ]
to_ = [1, 2, 2, 3, 2]
weight = [ 1, 10, 1, 1, 1 ]
c = 0
n = 4

import collections
def CountP(n, c, from_, to_, weight):
    
    dist = [float( 'inf' )] * n
    dist[c] = 0
    graph = {}
    weight_map = {}
    min_path = {c: [ [0] ]}
    for idx, a in enumerate( from_ ):
        b = to_[idx]
        weight_map[ (a, b) ] = weight[idx]
        weight_map[ (b, a) ] = weight[idx]
        graph.setdefault( a, [] )
        graph.setdefault( b, [] )
        graph[a].append(b)
        graph[b].append(a)
        
    que = collections.deque()
    for a in graph[c]:
        min_path.setdefault( a, [] )
        dist[ a ] = min( dist[a], weight_map[ (c, a) ] )
        min_path[a].append( [c, a] )
        que.append( [ c, a ] )
        
    while que:
        #print(que)
        path = que.popleft()
        node = path[-1]
        
        for next_ in graph[ node ]:
            min_path.setdefault( next_, [] )
            new_dist = dist[node] + weight_map[ (node, next_) ]
            if new_dist == dist[next_]:
                min_path[next_].append( path + [ next_ ] )
            if new_dist < dist[next_]:
                dist[next_] = new_dist
                min_path[next_] = [ path + [ next_ ] ]
                que.append( path + [ next_ ] )
                
    
    return min_path
    

print( CountP(n, c, from_, to_, weight) )
