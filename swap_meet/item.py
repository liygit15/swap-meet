import uuid

condition_description = {
    0: "heavily used",
    1: "used",
    2: "fair",
    3: "good",
    4: "like new",
    5: "mint"
}

age_description = {
    0: "more than 10 years",
    1: "more than 5 years but not more than 10 years",
    2: "more than 2 years but not more than 5 years",
    3: "more than 1 years but not more than 2 years",
    4: "more than 3 months but not more than 1 year",
    5: "new"
}


# wave 2
class Item:
    def __init__(self, id = None, condition = 0, age = None):
        # try:
        self.id = uuid.uuid4().int if id is None else int(id)
        # except TypeError as err:
        #     print("You should input an integer not others.")



        self.condition = condition
        self.age = age 


    def get_category(self):
        # return "Item"   hard code , if there is subclass , that will still be Item, not flexible.
        return self.__class__.__name__  # __name__ to get the class name
    

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."  # same as get_category, there maybe hard code issue
    
    # wave 5 last one
    def condition_description(self):

        condition = self.condition
        return condition_description[condition]


    def age_description(self):

        age = self.age
        return condition_description[age]
    
    