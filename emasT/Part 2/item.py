class Item:
    def __init__(self, title, autor):
        self._title = title
        self._autor = autor
        self._lent = False
    
    def showInfo(self):
        return f"Item: {self._title}, Autor: ${self._autor}"
    
    def lend(self):
        if not self._lent:
            self._lent = True
            return True
        return False
    
    def getBack(self):
        if self._lent:
            self._lent = False
            return True
        return False

    @property
    def lent(self):
        return self._lent        