import display
import numpy

prime_numbers_upto_30 = [2,	3, 5, 7, 11, 13, 17, 19, 23, 29]
# prime_numbers = prime_numbers_upto_30

# def is_prime_number(limit, prime_numbers):    
#     if limit > 30:
#         prime_numbers = prime_numbers_upto_30
#         for number in range(30, limit):
#             flag = 0
#             for prime in prime_numbers:
#                 if number % prime == 0:
#                     flag = 1
#                     break
#             if flag == 0:
#                 prime_numbers.append(number)
#     else:
#         prime_numbers = []
#         for number in prime_numbers_upto_30:
#             if number < limit:
#                 prime_numbers.append(number)
#     return prime_numbers

def get_prime_numbers(limit, prime_numbers = [2, 3]):
    # limit += 1
    if limit > max(prime_numbers):
        # print(f"will check {limit} > {max(prime_numbers)} from {prime_numbers}")
        for number in range(max(prime_numbers)+1, limit+1):
            # print(f"for {number} in range of max {prime_numbers} for limit as {limit}")
            flag = 0
            for prime in prime_numbers:
                if number % prime == 0:
                    flag = 1
                    break
            if flag == 0:
                prime_numbers.append(number)
                print("LLL", number, limit)
    return prime_numbers

def process(limit):
    prime_numbers = get_prime_numbers(limit, [2, 3])
    return prime_numbers


def test():
    test_data = [
        {
            'limit': 30,
            'list': [2,	3, 5, 7, 11, 13, 17, 19, 23, 29],
        },
        {
            'limit': 90,
            'list': [
                2,	3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37,	41,	43,	47,	53,	59,	61,	67,
                71, 73, 79, 83, 89
            ],
        },
        {
            'limit': 15,
            'list': [2,	3, 5, 7, 11, 13],
        },
        {
            'limit': 3,
            'list': [2,	3],
        },
        {
            'limit': 5,
            'list': [2,	3, 5],
        },
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
    find_data = [
        {
            'limit': 300
        }
    ]
    new_data = {}
    for index, data in enumerate(find_data):
        sequence = process(limit=data['limit'])
        new_data[index] = [sequence, data['limit']]
    column_headers_list = ['list', 'limit']
    display.table(new_data, column_headers_list)


display.main(test, find_answer)