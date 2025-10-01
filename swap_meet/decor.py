# wave 5 module 2
import uuid
from .item import Item

class Decor(Item):
    def __init__(self, id = None, width = 0, length = 0, condition = 0, age = 0):
        # self.id = uuid.uuid4().int if id is None else id
        super().__init__(id = id, condition = condition, age = age)
        self.width = width 
        self.length = length if length else 0 # 有什么区别？和上下

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    

    