aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here - ('I', 'a', 'tuple')
    newTuples = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            newTuples = newTuples + (aTup[i],)
    return (newTuples)

print(oddTuples(aTup))