"""" Class to encapsulate the body and author of the quotes """


class QuoteModel:

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def print_quote(self):
        """ Prints the quote and author """
        print(f'{self.body} - {self.author}')