# main file
print("Hi Jeffrey.")

def prime_number_check(x):
    for i in range(2,x - 1):
        if x%i == 0:
            return False
    return True

# return the sum of the primes
def prime_number_sum(x):
    primes = []
    for i in range(2,10 * x + x * x * x):
        if prime_number_check(i):
            primes.append(i)
            a = sum(primes)
    return a






print(prime_number_sum(1))
print(prime_number_sum(5))
print(prime_number_sum(10))







