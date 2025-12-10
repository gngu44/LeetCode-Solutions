class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] in complexity[1::]:
            return 0
        if complexity[0] != min(complexity):
            return 0

        
        return factorial(len((complexity))-1)%1000000007

