# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
    ingrlist = ["flour", "eggs", "oil"]

    for ingredient in ingredients:

        if ingredient in ingrlist:
            ingrlist.remove(ingredient)
    if len(ingrlist) == 0:
        return True
    else:
        return False



print(can_make_pasta(["flour", "oil"]))
