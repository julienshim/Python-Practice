class Quote:
    def __init__(self, quote, author, link):
        self.text = quote
        self.author = author
        self.link = f"https://quotes.toscrape.com{link}"