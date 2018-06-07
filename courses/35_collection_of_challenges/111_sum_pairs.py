'''
write a function called sum_pairs which accepts a list and a number 
and returns the first pair of numbers that sum to the number passed to that function

sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(nums, total):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == total:
                return [nums[x], nums[y]]
    return []
        