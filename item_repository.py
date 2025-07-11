from models.item import Item  #importing the library models.item as Item because we are using data as items

class Itemrepository:  # we have taken function name as Itemrepository
    def __init__(self):     # here we are using the __init__ function because here we are numerical statement and self has argument
        self.items = {}
        self.counter = 1

    def create(self, name, description):  #here we can see that we have object has create and here we r using data has name nad description
        item = Item(str(self.counter), name, description)   # Now in this step string data type because here we need to give the name and description in the data
        self.items[item.item_id] = item  
        self.counter += 1
        return item
    
    def get_all(self):      # Here we are using the get method to create the data
        return[item.to_dict() for item in self.items.values()]
    
    def get_by_id(self, item_id):   # Here we are using get_by function because here we can see that we are getting the data by using Item_id
        item = self.items.get(item_id)
        return item.to_dict() if item else None
    
    def update(self, item_id, name, description):       # Here we are using the update function for updating the existing which is present
        if item_id in self.items:
            item = self.items[item_id]
            item.name = name
            item.description = description
            return item.to_dict()
        return None
    
    def delete(self, item_id):
        return self.items.pop(item_id, None) is not None
    
from models.item import Item

class ItemRepository:
    def __init__(self):
        self.items = {}
        self.counter = 1