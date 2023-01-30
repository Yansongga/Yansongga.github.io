a = [29, 36, 57]
b = [25, 18, 3]

def xor( a, b):
    out = [] 
    for idx in range( len(a) ):
        x, y = a[idx], b[idx]
        
        find = False
        for i in range( x+1 ):
            j = x - i
            if (i^ j) == y:
                find = True
                break
            
        if find == True:
            out.append( 2 * i + 3 *j )
        else:
            out.append(0)
            
    return out
    
print( xor(a, b) )
