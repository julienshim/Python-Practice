from random import randint

class Author:
    def __init__(self, born_date, born_location, description_arr):
        self.born_date = f"This person was born on {born_date}."
        self.born_location = f"This person was born {born_location}."
        self.description_arr = description_arr

    def get_random_fact(self):
        len_desc_arr = len(self.description_arr)-1
        return self.description_arr[randint(0, len_desc_arr)]
