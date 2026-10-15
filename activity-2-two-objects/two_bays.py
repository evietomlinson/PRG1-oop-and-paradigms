"""
Two bays, one class.

The same class as activity 1, used twice. The interesting part is
what each object knows, and what the word self is actually doing.
"""


class Bay:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.registration = None

    def is_free(self):
        return self.registration is None

    def park(self, registration):
        if self.registration is None:
            self.registration = registration
            return True
        return False

    def describe(self):
        if self.registration is None:
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"

bays = [
    Bay(1, "standard"),
    Bay(2, "accessible"),
    Bay(3, "standard")
]

for bay in bays:
    print(bay.describe())

first = Bay(1, "standard")
second = Bay(2, "accessible")
forth = Bay(3, "standard")

first.park("AB12 CDE")


print(first.is_free())
print(second.is_free())
print(forth.is_free())

print(first.number, second.number, forth.number)

second.park("XY99 ZZZ")
print(second.describe())

forth.park("EA14 WZV")
print(forth.describe())

