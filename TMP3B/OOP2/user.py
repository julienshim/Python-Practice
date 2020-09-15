class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

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


class Moderator(User):

    active_moderators = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.active_moderators += 1

    @classmethod
    def display_active_moderators(cls):
        return f"There are currently {cls.active_moderators} active moderators."  # noqa

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community."  # noqa


u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)
jasmine = Moderator("Jasmine", "O'Conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'Conner", 61, "Piano")
print(User.display_active_users())
print(Moderator.display_active_moderators())

# print(jasmine.full_name())
# print(jasmine.community)
