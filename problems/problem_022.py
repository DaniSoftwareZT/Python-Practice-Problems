# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(day_of_week, is_sunny):

    # list1 = "umbrella"
    # list2 = "laptop"
    # list3 = "surfboard"

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekends = ["Saturday", "Sunday"]
    backpack = []

    for day in weekdays:
        if day_of_week == day and not is_sunny:
            backpack.append("umbrella")

        if day_of_week == day:
            backpack.append("laptop")

    for day in weekends:
        if day_of_week == day:
            backpack.append("surfboard")


    return backpack




    # if not is_sunny and is_workday:
    #     return list1
    # if is_workday:
    #     return list2
    # if not is_workday:
    #     return list3

print(gear_for_day("Monday", False))
