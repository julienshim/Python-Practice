name = 'Jerauld Manansala'
age = 34
height = 72 #inches 
height_converted_to_centimeters = round(height * 2.54) #centimeters
weight = 200 #lbs
weight_converted_to_kilograms = round (weight * 0.453592) #kilograms
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height_converted_to_centimeters} inches tall.")
print(f"He's {weight_converted_to_kilograms} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height_converted_to_centimeters + weight_converted_to_kilograms
print(f"If I add {age}, {height_converted_to_centimeters}, and {weight_converted_to_kilograms} I get {total}.")