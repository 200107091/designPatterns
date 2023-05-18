class Item:
    def __init__(self, title: str, author: str, num_copies: int):
        self.title = title
        self.author = author
        self.num_copies = num_copies

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_num_copies(self) -> int:
        return self.num_copies

    def check_availability(self) -> bool:
        return self.num_copies > 0


class Book(Item):
    def __init__(self, title: str, author: str, num_copies: int, ISBN: str):
        super().__init__(title, author, num_copies)
        self.ISBN = ISBN

    def get_ISBN(self) -> str:
        return self.ISBN


class Magazine(Item):
    def __init__(self, title: str, author: str, num_copies: int, issue_num: int):
        super().__init__(title, author, num_copies)
        self.issue_num = issue_num

    def get_issue_num(self) -> int:
        return self.issue_num


class CD(Item):
    def __init__(self, title: str, author: str, num_copies: int, genre: str):
        super().__init__(title, author, num_copies)
        self.genre = genre

    def get_genre(self) -> str:
        return self.genre


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def search_by_title(self, title: str):
        return [item for item in self.items if item.get_title() == title]

    def search_by_author(self, author: str):
        return [item for item in self.items if item.get_author() == author]


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password