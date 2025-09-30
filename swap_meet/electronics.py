# wave 5 module 3
import uuid
from .item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0):
        # self.id = uuid.uuid4().int if id is None else id
        super().__init__(id = id, condition = condition)
        self.type = type 
        

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
