# Create a prime_finder() function that takes in a number, n, and returns all the prime numbers from 1 to n (inclusive). As a reminder, a prime number is a number that is only divisible by 1 and itself.
# For example, prime_finder(11) should return [2, 3, 5, 7, 11].

# function to check if each number is prime.
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return False if (n <= 1 or n % i == 0) else True

# Function to cycle through each number from 1 to n.
# Returns an array of prime numbers.


def prime_finder(n):
    num = 2
    holder = []
    for i in range(1, n+1):
        testNum = isPrime(i)
        if(testNum == True):
            holder += [i]
    return holder


print(prime_finder(11))
