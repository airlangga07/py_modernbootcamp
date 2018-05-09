def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_all_values(1, 30, 2, 3, 4)

nums = [1, 2, 3, 4, 5, 6]

sum_all_values(*nums)
