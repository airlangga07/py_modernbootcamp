# our first example
numbers = dict(first=1, second=2, third=3)
squared_numbers = { key: value ** 2 for key, value in number.items() }
print(squared_numbers) # { 'first': 1, 'second': 4, 'third': 9 }

# more examples
str1 = '123'
str2 = 'abc'

combo = { str1[i]: str2[i] for i in range(len(str1)) }
print(combo) # { '1': 'a', '2': 'b', '3': 'c' }

# conditional logic with dictionaries
num_list = [1, 2, 3, 4]

is_odd_even = { num: ("even" if num % 2 == 0 else "odd") for num in num_list }
print(is_odd_even) # { '1': 'odd', '2': 'even', '3': 'odd', '4': 'even' }
