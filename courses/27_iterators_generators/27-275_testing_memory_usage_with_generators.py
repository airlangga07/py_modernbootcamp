def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

def fib_gen(max):
    count = 0
    x, y = 0, 1
    while count < max:
        x, y = x, x + y
        yield x
        count += 1

for n in fib_list(10):
    print(n)
