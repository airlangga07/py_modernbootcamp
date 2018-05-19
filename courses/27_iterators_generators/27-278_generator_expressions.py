import time
# generator expressions
# example
# def nums():
#     for num in range(1, 10):
#         yield num

# you can do that in single line
# g = (num for num in range(1, 10))

# simple time check
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_stop_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_stop_time = time.time() - list_start_time

print(gen_stop_time)
print(list_stop_time)