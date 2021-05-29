from random import randint
from resources.determine_last_name import determine_last_name

class Author:
    def __init__(self, name, born_date, born_location, description_arr):
        self.name = name
        self.born_date = born_date
        self.born_location = born_location
        self.description_arr = description_arr

    def get_last_name_hint(self):
        last_name = determine_last_name(self.name)
        hidden_last_name = last_name[0] + len(last_name[1:]) * '*'
        return f"This person's last name is {hidden_last_name}."
    
    def get_born_date_hint(self):
        return f"This person was born on {self.born_date}."

    def get_born_location_hint(self):
        return f"This person was born {self.born_location}."

    def get_random_bio_fact(self):
        len_desc_arr = len(self.description_arr)-1
        return self.description_arr[randint(0, len_desc_arr)]

    def get_all_author_hints(self):
        return [self.get_last_name_hint(), 
                self.get_born_date_hint(),
                self.get_born_location_hint(),
                ] + self.description_arr
