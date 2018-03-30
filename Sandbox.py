# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = person("otti",20)
# p2 = person("otti2",30)

# allPersons = [p1,p2]

# for person in allPersons:
#     print(person.name)
#     print(person.age)


# def manual_sum(factor, *args):
#     sum = 0
#     for x in args:
#         sum += x
#     return factor * sum

# l = [1, 2, 3, 4]
# s4 = manual_sum(*l)

# print(s4)

# point = (3, 8, 2)
# coordinates = {'x': 8, 'y': 33, 'z': -4}

# def set_destination(*args, **kwargs):
#     """Function takes a variable number of positional and keyword
#        arguments and prints the destination coordinates."""
#     # print(f'Goint to x={args[0]},y={args[1]},z={args[2]}')
#     tmp = ",".join("=".join((k,str(v))) for k,v in sorted(coordinates.items()))
#     print(tmp)

# set_destination(**coordinates)

# values = {"a":3, "b":2, "c":4}
# some_values = {"c": 7, "b": 4}

# def product(*args, **kwargs):
#     """Function that returns the product of all arguments, both,
#        for positional and keyword arguments."""
#     prod = 1
#     for x in args:
#         prod *= x
#     for k,v in kwargs.items():
#         prod *= v
#     return prod
 
# result = product(1, **some_values)
# print(result)


# def val_for_longest_key(**kwargs):
#     """Function that returns the value of the keyword argument with the
#        longest name."""
#     # YOUR CODE HERE
#     maxLen = 0
#     maxValue = 0
#     for k,v in kwargs.items():
#         print(len(k))
#         if len(k) > maxLen:
#             maxLen = len(k)
#             maxValue = v
#     return maxValue

# val_for_longest_key(foo=10, alpha=3, x=9)


import random
num_digits = 5
random_digits = map(lambda _: random.randint(0, 9), range(num_digits))

digit_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}