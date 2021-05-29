from resources.load_resources import load_resources
from resources.get_author_info import get_author_info
from resources.generate_possible_answers import generate_possible_answers
from random import randint

class QuoteManager:
    quote_number = 0
    author_info = {}
    four_author_hints = []
    hint_number = 0

    def __init__(self):
        self.quotes = load_resources()
        self.get_author_info()
        self.load_four_author_hints()
        
    def get_quote(self):
        return self.quotes[self.quote_number].quote

    def get_quote_author(self):
        return self.quotes[self.quote_number].quote_author

    def get_author_info(self):
        self.author_info = get_author_info(self.quotes[self.quote_number].quote_author_bio_link)

    def navigate_next_quote(self):
        self.quote_number += 1
        self.get_author_info()
        self.load_four_author_hints()

    def get_answer_arr(self):
        return list(set(generate_possible_answers(self.get_quote_author()) + generate_possible_answers(self.author_info.name)))

    def get_all_author_hints(self):
        return self.author_info.get_all_author_hints()

    def load_four_author_hints(self):
        self.four_author_hints = []
        self.hint_number = 0
        all_author_hints = self.get_all_author_hints()
        while len(self.four_author_hints) < 4:
            hint = all_author_hints[randint(0, len(all_author_hints)-1)]
            if hint not in self.four_author_hints:
                self.four_author_hints.append(hint)

    def get_author_hint(self):
        return self.four_author_hints[self.hint_number]

    def navigate_next_hint(self):
        self.hint_number += 1



    
