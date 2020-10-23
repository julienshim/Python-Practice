def be_polite(fn):
    def wrapper():
        print("what a pleaseure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


@be_polite
def greet():
    print("My name is Blah.")


@be_polite
def rage():
    print("I HATE YOU!")


greet()
rage()
