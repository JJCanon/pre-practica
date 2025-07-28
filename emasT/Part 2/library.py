from item import Item

class Library:
    #Constructor
    def __init__(self):
        self.items = []
    
    # to add items
    def add_item(self,item):
        self.items.append(item)
    
    # to show items
    def display_items(self):
        for item in self.items:
            print(item.showInfo())
    # to lend items        
    def lendItem(self, title):
        for item in self.items:
            if item._title == title and not item.lent:
                return item.lend()
        return False
    # to get back items
    def getBackItem(self, title):
        for item in self.items:
            if item._title == title and item.lent:
                return item.getBack()
        return False
    
    