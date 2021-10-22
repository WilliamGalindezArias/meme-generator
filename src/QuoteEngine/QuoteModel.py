"""" Class to encapsulate the body and author of the quotes """


class QuoteModel(object):

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        """ returns a string representation of the object """
        print(f'{self.body} - {self.author}')

    def print_quote(self):
        """ Prints the quote and author """
        print(f'{self.body} - {self.author}')

    def __str__(self):
        return f"QuoteModel - '{self.body}' by {self.author}"