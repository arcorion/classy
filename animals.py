class Animals:

    def __init__(self, type="cat", count=10):
        self.type = type
        self.count = count

    def report(self, additional=0):
        total_animals = self.count + additional
        print(f"Between you and me, we have {total_animals} {self.type}s.")