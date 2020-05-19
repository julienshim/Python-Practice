# Define speak below:

sound = {
    "pig": "oink",
    "duck": "quack",
    "cat": "meow",
    "dog": "woof"
}


def speak(animal="dog"):
    return sound[animal] if animal in sound.keys() else "?"

# alt

# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"


# alt 2

# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"
