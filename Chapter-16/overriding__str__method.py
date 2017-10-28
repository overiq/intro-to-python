class Jester:
    def laugh(self):
        return "laugh() called"

    def __str__(self):
        return "A more helpful description"

obj = Jester()
print(obj)