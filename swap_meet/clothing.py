#wave 5 module 1
# import uuid
from .item import Item

class Clothing(Item):
    def __init__(self ,fabric = None, id = None, condition = 0, age = 0):
        # self.id = uuid.uuid4().int if id is None else id
        super().__init__(id = id, condition = condition, age = age)
        self.fabric = fabric if fabric else "Unknown"  # 不太会这部分

    # def get_category(self):
    #     return "Clothing"
    
    def __str__(self):
        str_from_item = super().__str__()
        return f"{str_from_item} It is made from {self.fabric} fabric."

    