# LC with conditional logic
# filtering
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 == 1]

# process during the insertion
halves = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]

# we can use in keyword as well
with_vowels = 'This is so much fun!'
without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
print(without_vowels)
