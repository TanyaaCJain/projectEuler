import pandas

def table(data, column_headers_list):
    table = pandas.DataFrame.from_dict(data, orient='index',
                                       columns=column_headers_list)
    print(table)

def main(test, find_answer):
    import time
    start_time = time.time()
    print("TEST")
    print("-------------")
    test()
    print("")
    print("FIND DATA")
    print("-------------")
    find_answer()
    print("")
    print("--- %s seconds ---" % (time.time() - start_time))