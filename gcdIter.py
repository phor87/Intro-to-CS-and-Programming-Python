def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        smallest = b
    else:
        smallest = a
    while a % smallest >= 1 or b % smallest >= 1:
        smallest -= 1
    return smallest