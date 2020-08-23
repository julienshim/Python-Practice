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

    def __repr__(self):
        return f"{self.first} is {self.age} years old."

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


tom = User.from_string("Tom,Jones,89")
print(tom)

j = User("judy", "steele", 18)
j = str(j)
print(j)
