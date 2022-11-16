# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(scores):

    print(scores)

    if sum(scores) / len(scores) >= 90:
        return "A"
    elif sum(scores) / len(scores) >= 80:
        return "B"
    elif   sum(scores) / len(scores) >= 70:
        return "C"
    elif sum(scores) / len(scores) >= 60:
        return "D"
    else:
        return "F"

print(calculate_grade([99, 82, 35]))
