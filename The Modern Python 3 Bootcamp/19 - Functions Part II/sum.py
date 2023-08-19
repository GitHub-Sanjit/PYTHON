def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all_nums(8,9,6,7,9,4))