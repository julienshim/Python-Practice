class GrumpyDict(dict):
    def __repr__(self):
        return "NONE OF YOUR BUSINESS!"

    def __missing__(self, key):
        return f"YOU WANT '{key.upper()}'? WELL IT AIN'T HERE!"

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OKAY, FINE!")
        super().__setitem__(key, value)

    def __contains__(self, item):
        return "NO, IT AIN'T HERE!"
        return False


data = GrumpyDict({
    "name": "Tom",
    "animal": "cat"
})

print(data)
data['city'] = 'Seoul'
print(data['city'])
print(data)
