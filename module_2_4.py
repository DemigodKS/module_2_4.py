numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for a in range(len(numbers)):
    primes_ = [a + 1 for a in range(len(numbers))]
    # print(primes_)
    break

for k in range(2, len(primes_)):
    primes = [k for k in range(2, len(primes_)) if k // 2 == 1 or k % 2 != 0 and k % 3 != 0]
    print("Primes:",primes)
    break

for i in range(len(numbers)):
    not_primes_ = [i for i in range(len(numbers))]
    # print(primes_)
    break

for j in range(3, len(not_primes_)):
    not_primes = [j + 1 for j in range(3, len(not_primes_)) if j % 3 == 2 or j % 2 == 1]
    print("Not Primes:",not_primes)
    break

