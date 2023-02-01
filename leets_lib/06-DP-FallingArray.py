class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        k = 1 
        dp = {}
        m, n = len(matrix), len( matrix[0] )
        tmp = matrix[ -1 ]

        for i in range( m-2, -1, -1 ):
            new_tmp = []
            for j in range( n ):
                cols = [ col for col in range(j-k, j+k+1)
                     if -1 < col < n ]
                cost = [ matrix[i][j] + tmp[col] for col in cols ]
                new_tmp.append( min(cost) )
            tmp = new_tmp

        return min(tmp)
