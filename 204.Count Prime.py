class Solution(object):
    def countPrimes(self, n):
        count = 0
        if n <= 2:
            return count
        for i in range(3, n):
            for j in range(2, i):
                if i % j == 0:
                    count = count - 1
                    break
            count = count + 1
        return count + 1

    def countPrimes1(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


a = Solution()
print(a.countPrimes(49979))
print(a.countPrimes1(49979))
