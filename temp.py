import collections

counter = collections.Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(counter['apple'])  # Output: 3
print(counter.most_common(2))  # Output: [('apple', 3), ('banana', 2)]
