import uuid

description = {
    0: "heavily used",
    1: "used",
    2: "fair",
    3: "good",
    4: "like new",
    5: "mint"
}


# wave 2
class Item:
    def __init__(self, id = None, condition = 0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition


    def get_category(self):
        # return "Item"   hard code , if there is subclass , that will still be Item, not flexible.
        # return self.__class__.__name__  # __name__ 是为了获得class的名字。
        return "Item"   
    

    def __str__(self):
        return f"An object of type Item with id {self.id}."  # same as get_category, there maybe hard code issue
    
    # wave 5 last one
    def condition_description(self):

        condition = self.condition
        return description[condition]



    
    