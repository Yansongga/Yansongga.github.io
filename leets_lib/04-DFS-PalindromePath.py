A = ['z', 'a', 'a', 'a']

from_ = [0, 0, 1]
to_ = [1, 2, 3]

que = [3]
import collections

def path( A, from_, to_, que ):
    n = len(A)
    
    def check(s_):
        all_char = set()
        d = {}
        for a in s_:
            d.setdefault( a, 0 )
            d[a] += 1
            all_char.add(a)
            
        num_odd = 0
        for c in all_char:
            if d[c] % 2 ==1:
                num_odd +=1
        if num_odd <2:
            return True
        else:
            return False
            
      
        
    def answer( node ):
        stack = [[node]]
    
        while len(stack)> 0:
            path = stack.pop()
            des = path[-1]
            if des == 0:
                res = path
            else:
                for idx, i in enumerate(to_):
                    if des == i:
                        j = from_[ idx]
                        new_path = path + [j]
                        stack.append( new_path )
        
        #print( res )
        
        char = [ A[idx] for idx in res ]
        v = 0
        for idx in range( len(char) ):
            res = check( char[ : idx+1 ] )
            if res == True:
                v+=1
        return v 
        
    out = []
    for q in que:
        out.append( answer( q ) )
    return out
    
    
print( path( A, from_, to_, que ) )
