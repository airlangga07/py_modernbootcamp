# using the raise error to throw a custom error of your own
# for example
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")

    if type(color) is not str:
        raise ValueError("Color must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    if type(text) is not str:
        raise TypeError("Text must be an instance of str")

    print('Printed {} in {}'.format(text, color))

colorize('hello', 'red')
colorize(23, 'red')
colorize('hello', 23)
