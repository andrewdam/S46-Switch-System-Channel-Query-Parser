test_in = [
    '[@1,8,15,24]',
    '[@24]',
    '[@16,19]',
    '[@]',
    '[@1]',
    '[@15]'
    ]

def f(str_in):
    
    lst_in = map(int, str_in[2:-1].split(',')) if len(str_in) > 3 else []
    
    result = [0] * 4
    for x in lst_in:
        result[(x-1)/6] = x
    return result

for t in test_in:
    res = f(t)
    print 'Original: {}'.format(t)
    print 'Result: {}, {}, {}, {}'.format(res[0], res[1], res[2], res[3])

        
