class Quote:
    def __init__(self, quote, quote_author, quote_author_bio_link):
        self.quote = quote
        self.quote_author = quote_author
        self.quote_author_bio_link = f"https://quotes.toscrape.com{quote_author_bio_link}"