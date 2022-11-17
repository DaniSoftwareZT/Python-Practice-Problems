# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):

    if len(values) == 0:
        return None
    elif len(values) == 1:
        return None

    mx = max(values[0], values[1])
    secondmax = min(values[0], values[1])
    n= len(values)
    for i in range(2, n):
        if values[i] > mx:
            secondmax = mx
            mx = values[i]
        elif values[i] > secondmax and mx != values[i]:
            secondmax = values[i]
        elif mx == secondmax and secondmax != values[i]:
            secondmax = values[i]
    return secondmax

print(find_second_largest([3, 24, 9, 12, 46, 12]))
