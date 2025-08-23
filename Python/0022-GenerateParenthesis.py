class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(nOpen, nClosed, s):
            if len(s) == n * 2:
                out.append(s)
                return

            if nOpen < n:
                dfs(nOpen + 1, nClosed, s + "(")

            if nClosed < nOpen:
                dfs(nOpen, nClosed + 1, s + ")")
                
        out = []
        dfs(0, 0, "")
        return out