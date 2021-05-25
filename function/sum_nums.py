def sum_nums(*args):
    data=0
    for i in args:
        data += i
    data_mean= data / len(args)
    
    print(f'합은: {data} 평균: {data_mean}')
    return data, data_mean


sum_nums(10,20,30)
sum_nums(10,20,30,40,50)