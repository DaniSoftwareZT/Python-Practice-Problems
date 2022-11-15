# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    list1 = "umbrella"
    list2 = "laptop"
    list3 = "surfboard"

    if not is_sunny and is_workday:
        return list1
    if is_workday:
        return list2
    if not is_workday:
        return list3

print(gear_for_day("Friday", "No"))
