def tags(cls):
    class wrapper(cls):
        def __init__(self, *vArgs, **kwArgs):
            super().__init__(*vArgs, **kwArgs)
            self._tags = []

        @property
        def tags(self):
            return self._tags
        
        @tags.setter
        def tags(self, value):
            self._tags.append(value)

    return wrapper




@tags
class Integer:
    def __init__(self, value) -> None:
        self.val = int(value)
    
    def __str__(self):
        return str(self.val)

i1 = Integer(10)
i2 = Integer("20")
print(i1, i2)

i1.tags = "Python"
i1.tags = "Tuesday"

print(i1.tags)