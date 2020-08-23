class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    # always need self

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing.lower()}."

    def is_senior(self):
        return self.age > 65

    def birthday(self):
        self.age += 1
        end = ""
        if str(self.age)[-1] == "1":
            end = "st"
        elif str(self.age)[-1] == "2":
            end = "nd"
        elif str(self.age)[-1] == "3":
            end = "rd"
        else:
            end = "th"
        return f"Happy {self.age}{end} Birthday, {self.first}!"


# print(user1.display_active_users())
print(User.display_active_users())

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(User.display_active_users())
