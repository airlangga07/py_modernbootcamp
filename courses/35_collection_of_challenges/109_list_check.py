'''
write a function called list_check, which accepts a list and 
returns True if each value in the list is a list, otherwise the function should return false

list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(input_list):
    for value in input_list:
        if type(value) is not list:
            return False
    return True