class Solution:
    def findTheWinner(self,n: int, k: int) -> int:
        return self.sol(n, k) + 1  

    def sol(self, n1: int, k1: int) -> int:
        if n1 == 1:
            return 0
        return (self.sol(n1 - 1, k1) + k1) % n1
        