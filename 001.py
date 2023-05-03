import pandas
import display

def get_sequence(start=1, skip=1, limit=10):
    sequence = []
    for index in range(limit):
        term = start + (index*skip)
        if term < limit:
            sequence.append(term)
    return sequence

def sum_of_arithmetic_progression(a=1, d=1, n=10):
    if a < n:
        sum = (n/2)*((2*a) + ((n-1)*d))
    else: sum = 0
    return int(sum)

def process(start=1, skip=1, limit=10):
    sequence = get_sequence(start, skip, limit)
    if len(sequence) > 1:
        sum = sum_of_arithmetic_progression(
            a=sequence[0],
            d=sequence[1]-sequence[0],
            n=len(sequence)
        )
    else: sum = sequence[0]
    return sum

def main(limit):
    sequence_sum_of_3 = process(start=0, skip=3, limit=limit)
    sequence_sum_of_5 = process(start=0, skip=5, limit=limit)
    sequence_sum_of_15 = process(start=0, skip=15, limit=limit)
    total_sum = sequence_sum_of_3 + sequence_sum_of_5 - sequence_sum_of_15
    return total_sum


def test():
    test_data = [{
        'limit': 10,
        'sum': 23,
    }]
    new_data = {}
    for index, data in enumerate(test_data):
        sum = main(limit=data['limit'])
        if sum == data['sum']:
            new_data[index] = ['pass', sum, data['sum']]
        else:
            new_data[index] = ['fail', sum, data['sum']]
    column_headers_list = ['check', 'calculated', 'answer']
    display.table(new_data, column_headers_list)
    
def find_answer():
    find_data = [
        {
            'limit': 1000
        }
    ]
    new_data = {}
    for index, data in enumerate(find_data):
        sum = main(limit=data['limit'])
        new_data[index] = [sum, data['limit']]
    column_headers_list = ['calculated', 'limit']
    display.table(new_data, column_headers_list)


display.main(test, find_answer)
