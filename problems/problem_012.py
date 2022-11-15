# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
    word1 = "fizbuzz"
    word2 = "fizz"
    word3 = "buzz"

    if number % 3 ==0 and number % 5 == 0:
        return word1
    if number % 3 == 0:
        return word2
    if number % 5 == 0:
        return word3
    else:
        return number

print(fizzbuzz(30))
