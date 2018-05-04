for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    elif num % 2 == 1:
        state = "odd"
    print("{} is {}".format(num, state))
