import doctest

def add_numbers(a, b):
    ''' (int, int) --> int
    >>> add_numbers(bob, 1)
    2
    >>> add_numbers(2, 2)
    4
    '''
    return a + b

def subtract_numbers(a, b):
    ''' (int, int) --> int 
    >>> subtract_numbers(3, 1)
    2
    '''  
    return a - b


def verify_part_number(raw_part_number):
    '''  (str) --> str
    >>> verify_part_number('foo')
    'YES'
    >>> verify_part_number('-')
    'NO'
    '''
    if '-' in raw_part_number:
        return 'NO'
    else:
        return 'YES'

runner = doctest.DocTestRunner()