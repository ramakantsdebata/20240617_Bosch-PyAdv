def Bar():
    print("Bar")

def Foo():
    print("Foo")
    Bar()

def Main():
    x = 1
    print("Main", x)
    Foo()
    x +=  1
    print("Main", x)

def Test1():
    print("About to call Main")
    Main()
    print("Returned from Main")

##################################################


class MyType:
    def __init__(self) -> None:
        self.x = 1

    def display(self):
        print(self.x)

def Test2():
    obj = MyType()
    obj.display()

################################################
'''
# C - code
int add (int a, int b)
{
    return a + b;
}

struct MyType
{
    int x;
    int y;
    int(*pAdd)(int, int);
};


void F2(struct MyType obj)
{
    obj.x = 10
}

void F1(/*OUT*/ struct MyType**  data)
{
    struct MyType t1;
    t1.x = 1;
    t1.y = 2;
    t1.pAdd = add;

    *data = &t1
    F2(t1)
    printf("%d", t1.x)
}

void F1B(/*OUT*/ struct MyType**  data)
{
    struct MyType* t1;
    t1 = (struct MYType*)malloc(sizeof(structM MyType))
    t1->x = 1;
    t1->y = 2;
    t1->pAdd = add;
    *data = t1
    F2(t1)
    printf("%d", t1.x)
}

void F0()
{
    struct MyType * ptr = NULL;
    F1(&ptr)
    printf("%d", ptr->x);
}
'''