from typing import Any
import random

class PrimeGenerator:
    def pow_with_mod(a,b, mod):
        if mod == 1:
            return 0
        result = 1
        base = a % mod
        while b > 0:
            if (b % 2 == 1):
                result = (result * base) % mod
            b = b >> 1
            base = (base * base) % mod
        return result

    def rabin_test(number, k = 5):
        if number % 2 == 0:
            return False
        m = (number - 1) // 2
        t = 1
        while m % 2 == 0:
            m //= 2
            t = t + 1
        for _ in range(k):
            a = random.randint(2, number - 1)
            u = PrimeGenerator.pow_with_mod(a, m, number)
            j = 1
            if (u == 1):
                continue
            while u != 1 and j <= t:
                u = PrimeGenerator.pow_with_mod(u, 2, number)
                j = j + 1
            if( u != 1 ):
                return False
        return True
    
    def ferma_test(number, k = 100000):
        if number <= 1 or number % 2 == 0:
            return False
        for _ in range(k):
            a = random.randint(2, number - 1)
            if PrimeGenerator.pow_with_mod(a, number - 1, number) != 1:
                return False
        return True
    
    def generate_probable_prime(size):
        p = random.randrange(10 ** (size - 1), 10**size - 1)
        if p % 2 == 0:
            p += 1
        min_num = p
        while True:
            p += 2
            if(p >= 10**size):
                p = random.randrange(10 ** (size - 1), min_num)
                if p % 2 == 0:
                    p += 1
                if(min_num > p):
                    p = min_num
            if not PrimeGenerator.ferma_test(p):
                continue
            return p    


    def __call__(self, size) -> Any:
        return PrimeGenerator.generate_probable_prime(size)