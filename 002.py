import display

def process(limit):
    sequence = [1, 2]
    index = 3
    term = 3
    print(limit)
    while(term <= limit):
        sequence.append(term)
        term = sequence[index - 1] + sequence[index - 2]
        index+=1
    sum = 0
    for item in sequence:
        if item % 2 == 0:
            sum += item
    return [sequence, sum]

def test():
    test_data = [{
        'limit': 100,
        'list': [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        'sum': 44
    }]
    new_data = {}
    for index, data in enumerate(test_data):
        sequence, sum = process(limit=data['limit'])
        if sequence == data['list'] and sum == data['sum']:
            new_data[index] = ['pass', sequence, data['list'], sum, data['sum']]
        else:
            new_data[index] = ['fail', sequence, data['list'], sum, data['sum']]
    column_headers_list = ['check', 'calculated', 'answer', 'calculated_sum', 'sum']
    display.table(new_data, column_headers_list)

def find_answer():
    find_data = [
        {
            'limit': 4000000
        }
    ]
    new_data = {}
    for index, data in enumerate(find_data):
        sequence, sum = process(limit=data['limit'])
        new_data[index] = [sum, data['limit']]
    column_headers_list = ['calculated', 'limit']
    display.table(new_data, column_headers_list)


display.main(test, find_answer)