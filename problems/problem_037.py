# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"

def pad_left(number, length, pad):

    numstr = str(number)        # numstr is making the number chosen a string
    strleng = len(numstr)       # strleng is getting the len of our string which is numstr

    diference = length - strleng       # diference is the assigned variable to the equation. lenght in this case is 7 and strleng is 2 meaning the plus signs = 5
    result = pad * diference + numstr  # result is the assigned variable to equation.  pad in this case is +  then multiply by 5 + numstr which is the string 12= result

    return result


print(pad_left(12, 7, "+"))
