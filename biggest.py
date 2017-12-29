animals = { 'a': ['aardvark', 'aa', 'aaa', 'aaaa'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest_key = ''
    x = 0
    for key in aDict:
        if len(aDict[key]) > x:
            biggest_key = key
            x = len(aDict[key])
    return biggest_key

print(max(animals.values()))
print(len(animals['d']))
print(biggest(animals))