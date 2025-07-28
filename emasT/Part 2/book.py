from item import Item

class Book(Item):
    def __init__(self, title, autor, pages):
        super().__init__(title,autor)
        self._pages = pages 
        
    def showInfo(self):
        return f"Book - {super().showInfo()}, pages: {self._pages}"
    