from swap_meet import item # 应该import item 还是Item？

#wave 1 
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
    
        return item
    
    # wave 2 
    def get_by_id(self,id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    
    #wave 3
    def swap_items(self,other_vendor, my_item, their_item):
        if ((my_item not in self.inventory) or
            (their_item not in other_vendor.inventory)):
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)

        return True

    
    #wave 4
    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        # solution1 swap positon to make time complexity simple
        # self.inventory[0] , self.inventory[-1] = self.inventory[-1] , self.inventory[0]
        # other_vendor.inventory[0] , other_vendor.inventory[-1] = other_vendor.inventory[-1] , other_vendor.inventory[0] 
        
        # self.inventory.append(other_vendor.inventory[-1])
        # other_vendor.inventory.append(self.inventory[-2])
        # self.inventory.pop(-2)
        # other_vendor.inventory.pop(-2)

        # return True
        
        # solution2 swap positon to make time complexity small, use temp to store value which exchange
        temp = self.inventory[0]
        self.inventory[0] = other_vendor.inventory[0] 
        other_vendor.inventory[0] = temp

        return True

    # wave 6 method 1
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)
        
        return result
    
    # wave 6 method 2
    def get_best_by_category(self, category):
        highest_score = 0
        highest_item = None

        select_by_category = self.get_by_category(category)
        for item in select_by_category:
            if item.condition > highest_score:
                highest_score = item.condition
                highest_item = item

        return highest_item

    # wave 6 method 3
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.get_best_by_category(their_priority)  or  not other_vendor.get_best_by_category(my_priority) :
            return False
        
        other_vendor_best = other_vendor.get_best_by_category(my_priority)
        vendor_best = self.get_best_by_category(their_priority)
        # swap
        self.swap_items(other_vendor,vendor_best, other_vendor_best)

        return True
        
        
