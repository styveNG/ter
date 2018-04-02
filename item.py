class Item:
    def __init__(self,nomItem,spetech=None):
        self.nomItem=nomItem
        self.spetech=spetech
    def __repr__(self):
        return "{}: {}".format(self.nomItem, self.spetech)