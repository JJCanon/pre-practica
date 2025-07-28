from item import Item

class Magazine(Item):
    def __init__(self, title, autor, number):
        super().__init__(title,autor)
        self._number = number
        
    def __str__(self):
        return f"Magazine - {super().showInfo()}, Number: {self._number}"
    