from prime_numbers import get_prime_numbers
import display
import math
import random

# Function to calculate (base^exponent)%modulus
def modular_pow(base, exponent,modulus):
 
    # initialize result
    result = 1
 
    while (exponent > 0):
     
        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus
 
        # exponent = exponent/2
        exponent = exponent >> 1
 
        # base = base * base
        base = (base * base) % modulus
     
    return result
 
# method to return prime divisor for n
def PollardRho( n):
 
    # no prime divisor for 1
    if (n == 1):
        return n
 
    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2
 
    # we will pick from the range [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x
 
    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = (random.randint(0, 1) % (n - 1))
 
    # Initialize candidate divisor (or result)
    d = 1
 
    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):
     
        # Tortoise Move: x(i+1) = f(x(i))
        x = (modular_pow(x, 2, n) + c + n)%n
 
        # Hare Move: y(i+1) = f(f(y(i)))
        y = (modular_pow(y, 2, n) + c + n)%n
        y = (modular_pow(y, 2, n) + c + n)%n
 
        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)
 
        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)
     
    return d


def pollard_rho(limit):

    def calc(d, c):
        return pow(d,2) + c

    def gcd(a, b):
        if a == 0 :
            return b
        
        return gcd(b%a, a)

    c = int(limit - math.sqrt(limit))
    x = c * 2
    
    # c = int(math.sqrt(limit))
    # x = int(math.sqrt(c))

    f_x = calc(x, c)
    f_y = calc(f_x, c)

    d = gcd(f_y - f_x, limit)
    return d

def gcd(a, b):
    if a == 0 :
        return b
    
    return gcd(b%a, a)

def general(limit):
    greatest_prime_factor = -1
    number = PollardRho(limit)
    print("divisor", number, limit % number)
    limit = int(limit/number)
    print(limit)
    prime_numbers = [2, 3, 5]
    number = min(prime_numbers)
    while(number < limit):
        print(f"will check {limit} > {max(prime_numbers)} from {prime_numbers}")
        prime_numbers = get_prime_numbers(number, prime_numbers)
        # print(prime_numbers)
        if number in prime_numbers:
            print(f"{number} is in {prime_numbers} for limit as {limit}")
            while(limit % number == 0):
                limit = int(limit / number)
                greatest_prime_factor = number
                print("ggg", greatest_prime_factor)
        number+=1
    # for number in range(limit):
    #     while(limit % number == 0):
    #         limit = limit / number
    #         greatest_prime_factor = number
    #     if number >= limit:
    #         break
    return greatest_prime_factor

def general(limit):
    greatest_prime_factor = -1
    number = PollardRho(limit)

def process(limit):
    # return pollard_rho(limit)
    # return PollardRho(limit)
    return general(limit)


def test():
    test_data = [
        # {
        #     'limit': 13195,
        #     'list': 29,
        # }
        {
            'limit': 99,
            'list': 11,
        }
    ]
    new_data = {}
    for index, data in enumerate(test_data):
        sequence = process(limit=data['limit'])
        if sequence == data['list']:
            new_data[index] = ['pass', sequence, data['list']]
        else:
            new_data[index] = ['fail', sequence, data['list']]
    column_headers_list = ['check', 'calculated', 'answer']
    display.table(new_data, column_headers_list)

def find_answer():
    pass
    # find_data = [
    #     {
    #         'limit': 600851475143
    #     }
    # ]
    # new_data = {}
    # for index, data in enumerate(find_data):
    #     sequence = get_prime_numbers(limit=data['limit'])
    #     new_data[index] = [sequence, data['limit']]
    # column_headers_list = ['list', 'limit']
    # display.table(new_data, column_headers_list)


display.main(test, find_answer)