class Solution:
    def fib(self, n: int) -> int:
        arr = [0,1]
        sum = 0
        if n == 0: return 0
        if n == 1: return 1
        for i in range(2,30):
            arr.append(arr[i-1] + arr[i-2])
        sum = arr[n- 1] + arr[n - 2]    
        return sum
