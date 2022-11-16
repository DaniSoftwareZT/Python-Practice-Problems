# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):

    print(values)

    if len(values) != 0:
        return sum(values)

    else:
        return 'empty'

print(calculate_sum([2, 9, 20]))
