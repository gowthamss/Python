from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

# Coutner
li = [1, 2, 3, 4, 5, 6, 7, 7, 6, 5]
print(Counter(li))

sentence = 'Hi, how r u today!'
print(Counter(sentence))

# defaultdict
dictionary = defaultdict(lambda: 4, {'a': 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])
dictionary2 = defaultdict(lambda: 'no key available', {'c': 3, 'd': 4})
print(dictionary2['e'])


# OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)

# datetime
print(datetime.time(5, 42, 1))
print(datetime.date.today())

# array
arr = array('i', [1, 2, 3])
print(arr[1])
