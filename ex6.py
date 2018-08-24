# variable with a value of 10, f-string with types_of_people
types_of_people = 10
x = f"There are {types_of_people} types of people."

# 2 variables with string values, and a f-string with binary and do_not
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#print x and y strings
print(x)
print(y)

#repeat print x and y with f-strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

#using format method for a value stored in a variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

#2 variables and combined with printed
w = "This is the left side of..."
e = "a string with a ride side."

print(w + e)