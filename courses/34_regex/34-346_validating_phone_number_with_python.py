import re

def extract_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match: 
        return match.group()
    return None

def extract_all_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.search(input)
    if match: 
        return True
    return False

print(extract_phone("my number is 432 567-2345"))
print(extract_phone("my number is 432 567-2345234"))
print(extract_phone("432 567-2345234"))
print(extract_phone("432 567-2345234 test"))
print(extract_all_phone("432 567-2345 test 678 765-0987"))
# def is_valid_phone():