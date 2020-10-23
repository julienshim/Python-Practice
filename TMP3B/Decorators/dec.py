def be_polite(fn):
    def wrapper():
        print("what a pleaseure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


def greet():
    print("My name is Blah.")


def rage():
    print("I HATE YOU!")


greet = be_polite(greet)
greet()
greet()
greet()

polite_rage = be_polite(rage)
polite_rage()
polite_rage()
polite_rage()
