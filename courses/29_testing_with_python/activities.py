def eat(food, is_healthy):
    ending = "because YOLO"
    if is_healthy:
        ending = "because my body is a temple"
    return "I'm eating {}, {}".format(food, ending)

def nap(num_hours):
    if num_hours > 2:
        return "Ugh I overslept"
    return "I'm feeling refreshed after my 1 hour nap"
    pass