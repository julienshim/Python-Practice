# try:
# except:
# else:
# finally:

# while True:
#     try:
#         num = int(input('Please enter a number: '))
#     except ValueError:
#         print("Not a number.")
#     else:
#         print("A number has been entered.")
#         break
#     finally:
#         print("Finally runs no matter what.")
# print('Rest of the logic runs.')

# try:
#     num = int(input('Please enter a number: '))
# except:
#     print("Not a number.")
# else:
#     print("Else runs if except doesn't run.")
# finally:
#     print("Finally runs no matter what.")


def divide(a, b):
    try:
        result = a / b
    # except ZeroDivisionError:
    except (ZeroDivisionError, TypeError) as err:
        # print("Don't divide by zero, please.")
        # except TypeError as err:
        # print('A and B must Ints or Floats.')
        print('Something went wrong!')
        print(err)
    else:
        print(f'{a} divided by {b} is {result}')


print(divide(1, 'a'))
# print(divide(1,0))
print(divide(1, 0))
