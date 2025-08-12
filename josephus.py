class Solution:
    def josephus(self, n, k):
        # Base case: only one person remains
        if n == 1:
            return 1
        # Recursive case: adjust position based on elimination
        return (self.josephus(n - 1, k) + k - 1) % n + 1