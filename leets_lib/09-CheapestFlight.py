class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        cost = {}
        cost0 = [float('inf')] * n
        cost0[ src ] = 0
        
        cost[0] = cost0
        
        
        f_ = {}
        for f in flights:
            f_.setdefault( f[1], [] )
            f_[ f[1] ].append( f )
            
        
        
        for row in range(1, k+2):
            cost.setdefault( row, [] )
            for col in range(n):
                try:
                    f_list = [ cost[row-1][f[0]] + f[2] for f in f_[ col ] ]
                    f_list.append( cost[row-1][col] )
                   
                    cost[row].append(min( f_list ))
                except:
                    cost[row ].append( cost[row-1][ col ] ) 
        
        if cost[k+1][dst] == float('inf'):
            return -1
        
        return cost[k+1][ dst ]
                
