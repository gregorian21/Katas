-- Not a true Sieve of Eratosthenes, but generates primes nevertheless
primes x = sieve [] [2..x]
     where sieve ps []     = reverse ps
           sieve ps (x:xs) = sieve (x:ps) (filter (\n -> n `mod` x /= 0) xs)
