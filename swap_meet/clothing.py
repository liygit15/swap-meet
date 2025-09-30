#wave 5 module 1
# import uuid
from .item import Item

class Clothing(Item):
    def __init__(self ,fabric = None, id = None, condition = 0):
        # self.id = uuid.uuid4().int if id is None else id
        super().__init__(id = id, condition = condition)
        self.fabric = fabric if fabric else "Unknown"  # 不太会这部分

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."

    