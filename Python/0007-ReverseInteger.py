class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        con = False
        x = str(x)
        if x[0] == "-":
            x = x[1:]
            con = True
        
        y = ""
        for i in range(len(x)-1,-1,-1):
            y = y + x[i]

        while y[0] == 0:
            y.pop(0)
        if con:
            y = "-" + y

        y = int(y)
        if y <= (-2)**31 or y >= (2**31-1):
            return 0

        return y