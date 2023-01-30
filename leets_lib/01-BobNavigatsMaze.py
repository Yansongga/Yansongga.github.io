import collections
maze =  [ [0, 2, 0] , [2, 0, 2] , [0, 0, 0] ]
Alice = ( 2, 1 )

def path(maze, Alice):
    q = collections.deque()
    m, n = len(maze), len( maze[0] )
    coin_map = {}
    coin_count = 0
    for i in range(m):
        for j in range(n):
            if maze[i][j] ==2:
                coin_map[ (i, j) ] = coin_count
                coin_count += 1
    finish = 2 ** coin_count  -1
                
    ## state variable: 
    seen = set()
    if maze[0][0] == 2:
        start_state = (0, 0, 1)
        q.append( 0, 0, 1, 0)
    else:
        start_state = (0, 0, 0)
        q.append( (0, 0, 0, 0) )
        
    seen.add( start_state )
    #def shortestPath(maze, Alice):
    while q:
       
        i, j, coins, step = q.popleft()
        if i == Alice[0] and j == Alice[1] and coins == finish:
            return step
        
        dirs = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
        for d in dirs:
            a, b = i + d[0], j + d[1]
            if -1 < a < m and -1 < b < n and maze[a][b] != 1:
                if maze[a][b] == 2:
                    coin_id = coin_map[ (a, b) ] 
                    next_coins = coins | (2 ** coin_id)
                else:
                    next_coins =coins
                    
                if (a, b, next_coins) not in seen:
                    seen.add( (a, b, next_coins) )
                    q.append( (a, b, next_coins, step + 1) )
    #print(coin_map)           
    return -1
    
print( path(maze, Alice) )


                    
                    
                
            
    
   


    
    
    
