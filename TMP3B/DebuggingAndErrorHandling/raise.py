def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magneta")
    if type(text) is not str:
        raise TypeError('Text must be an instance of str')
    if type(color) is not str:
        raise TypeError('Color must be an instance of str')
    if color not in colors:
        raise ValueError('Color is invalid color')
    print(f'Printed {text} in {color}')


colorize('hello', 'yellow')
# colorize(123, 'red')
