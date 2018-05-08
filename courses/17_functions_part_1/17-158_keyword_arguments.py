# keyword arguments
def full_name(first, last):
    return "Your name is {} {}".format(first, last)

full_name(first='colt', last='steele')
full_name(last='steele', first='colt')

def exponent(num, power=2):
    return num ** power

print(exponent(power=3, num=5))
