method 1:
class Solution:
# @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
    
    method 2:
    class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        primes = [True for i in range(n+1)]
        count = 0
        p=2
        while p*p <= n:
            if primes[p]:
                for i in range(p*2 , n+1 , p):
                    primes[i]=False
                
            p += 1
        primes[0],primes[1] =False,False
        for p in range (n):
            if primes[p]:
                count+=1
        return count        
                
        
