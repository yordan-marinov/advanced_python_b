class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    @property
    def free_space(self):
        return self.size - self.quantity
    
    def enough_free_space_to_fill(self, value):
        return value <= self.free_space
    
    def fill(self, milliliters):
        if self.enough_free_space_to_fill(milliliters):
            self.quantity += milliliters
    
    def status(self):
        return self.free_space

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
