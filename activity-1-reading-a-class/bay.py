"""
One parking bay.

A class is a description of a kind of thing. This one describes a
single bay in a car park: what it knows about itself, and what it
can be asked to do.
"""


class Bay:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.registration = None
        self.cars_parked = 0 

    def is_free(self):
        return self.registration is None

    def park(self, registration):
        if self.registration is None:
            self.registration = registration
            self.cars_parked += 1 
            return True
        return False

    def leave(self):
        if self.registration is None: 
             print("The bay is empty.")
             return None
             
        leaving = self.registration
        self.registration = None
        return leaving

    def describe(self):
        if self.registration is None:
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"

    def size_matches(self, wanted): 
        wanted = "Standard"
        if self.size is wanted: 
            return True 
        return False


bay = Bay(1, "Standard")

print(bay.describe()) # bay 1 (standard )
print(bay.is_free()) #True

print(bay.park("AB12 CDE")) 
print(bay.describe()) #
print(bay.is_free()) #
print(bay.leave())

print(bay.park("XY99 ZZZ")) #
print(bay.describe()) #

print(bay.leave()) #
print(bay.describe()) #

print(bay.size_matches(""))
print(f"Cars that have used this bay: {bay.cars_parked}")

