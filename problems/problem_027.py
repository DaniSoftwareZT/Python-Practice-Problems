# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):

    for value in values:
        return max(values)

    else:
        return None

print(max_in_list([3, 9, 12]))
