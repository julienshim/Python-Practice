from random import randint
from resources.determine_last_name import determine_last_name

class Author:
    def __init__(self, name, born_date, born_location, description_arr):
        self.name = name
        self.born_date = f"This person was born on {born_date}."
        self.born_location = f"This person was born {born_location}."
        self.description_arr = description_arr

    def get_random_fact(self):
        len_desc_arr = len(self.description_arr)-1
        return self.description_arr[randint(0, len_desc_arr)]

    def get_last_name_hint(self):
        last_name = determine_last_name(self.name)
        return last_name[0] + len(last_name[1:]) * "*"