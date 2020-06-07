'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6" # noqa
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


# def calculate(make_float, operation, first, second, message="The result is"):
#     answer = 0
#     if operation == "add":
#         answer = first + second
#     elif operation == "subtract":
#         answer = first - second
#     elif operation == "multiply":
#         answer = first * second
#     elif operation == "divide":
#         answer = first / second
#     return "{} {}".format(message, float(answer) if make_float else int(answer))  # noqa


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), int(operation_value))
    return final
