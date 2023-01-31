
edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
n = 5
visit = [2, 4]
#print(visit.index(5))
import collections
def VisitNodesTree( n, edges, visit ):
    
    graph = {}
    for e in edges:
        i, j = e[0], e[1]
        graph.setdefault( i, [] )
        graph.setdefault( j, [] )
        graph[i].append(j)
        graph[j].append(i)
        
    que = collections.deque()
    v_bool = 0
    if visit[0] == 1:
        v_bool = 2 ** ( len(visit) -1 )
        
    state = ( 1, v_bool, 0 )   ## state variable node x v_bool x step
    seen = set()
    seen.add(( 1, v_bool) )
    
    que.append(state)
    shortest = float( 'inf' )
    finish = 2 ** ( len(visit) ) - 1 
    while que:
        node, v_bool, step = que.popleft()
        if node == n and v_bool == finish:
            shortest = min( shortest, step )
            
        for next_ in graph[node]:
            try:
                idx = visit.index( next_ )
                if idx == 0:
                    
                elif 0 not in v_bool[ : idx  ]::
                    new_bool = v_bool
                    new_bool[idx] = 1
                    new_state = ( next_, new_bool, step + 1 )
                    if ( next_, new_bool) not in seen:
                        seen.add( ( next_, new_bool) )
                        que.append( new_state )
                
            except:
                if ( next_, v_bool) not in seen:
                    seen.add( ( next_, v_bool) )
                    que.append( ( next_, v_bool, step+1) )
                    
    
    return shortest
    
print(VisitNodesTree( n, edges, visit ))
