# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations # noqa
total_donations = 0.0
for item in donations.items():
    total_donations += item[1]

# alt 1

# for donation in donations.values():
#  total_donations += donation

# adv alt 1

# total_donations = sum(donation for donation in donations.values())

# adv alt 2

# total_donations = sum(donations.values())
