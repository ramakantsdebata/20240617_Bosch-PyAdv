class Publisher:
    def __init__(self) -> None:
        self.collFn = []

    def Register(self, fn):
        self.collFn.append(fn)

    def __str__(self):
        return f"Functions in the collection --> {self.collFn}"
    
    def __len__(self):
        return len(self.collFn)
    
    def __getitem__(self, idx):
        return self.collFn[idx]
    
    def __add__(self, other):
        if isinstance(other, Publisher):
            obj = Publisher()
            obj.collFn = self.collFn + other.collFn
            # obj.collFn = list(self.collFn)
            # obj.collFn += other.collFn
            return obj
        else:
            raise TypeError("Needs to be of type Publisher")
    
    def Unregister(self, fn):
        self.collFn.remove(fn)

    def NotifyAll(self, data):
        for i in range(len(self)):
            self[i](data)


#############################################

def Foo(data):
    print("Foo -", data)

def Bar(data):
    print("Bar -", data)

def Baz(data):
    print("Baz -", data)
#--------------------------------------------

pub1 = Publisher()
pub1.Register(Foo)
pub1.Register(Bar)
print(len(pub1)) # pub1.__len__()
print(pub1)
# print(str(pub1))
# print(pub1.__str__())
# print(pub1.__repr__())

pub1.Unregister(Foo)
print(pub1)

try:
    pub1[0]("StringData")
except IndexError as ex:
    print(f"{ex!r}")

print("Resuming normal functioning")
pub1.Register(Foo)


pub1.NotifyAll("Time to wrap up")

pub2 = Publisher()
pub2.Register(Baz)

print("\n\n", "*" * 80)
pub3 = pub1 + pub2
pub3.NotifyAll("SomeEvent")