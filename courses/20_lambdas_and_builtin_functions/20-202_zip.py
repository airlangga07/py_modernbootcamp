# zip make an iterator that aggregates elements from each of the iterables
# returns an iterator of tuples, where the i-th tuple contains the i-th element from each
# of the argument sequences of iterables
# the iterator stops when the shortest input iterable is exhausted

first_zip = zip([1, 2, 3], [4, 5, 6])
print(list(first_zip))
print(dict(first_zip))

# another example
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

print(list(zip(nums1, nums2)))

# it does not to be in the same length, but it will be truncated
nums2 = [6, 7, 8, 9, 10, 11, 12]
print(list(zip(nums1, nums2)))

words = ['hi', 'lol', 'haha', 'lel']
print(list(zip(nums1, nums2, words)))

# unpacks the list of tuples
five_by_two = [(0, 1), (1, 2), (2, 3)]
list(zip(*five_by_two)) #[(0, 1, 2), (1, 2, 3)]

# another example
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# our target: {'dan': 98, 'ang': 91, 'kate': 78 }

# dict comprehension
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)
