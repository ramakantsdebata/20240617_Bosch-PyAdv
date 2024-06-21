__all__ = ['greet', 'greetName']

def greet():
    print("Hi there")

def greetName(name):
    greeting = "Hello"
    finalStr = CombineStr(greeting, name)
    print(finalStr)

def CombineStr(greeting, name):
    return greeting + " " + name + "!"

def Test():
    greet()
    greetName("Manish")

print(__name__)

if __name__ == "__main__":
    Test()



'''
> PrintName Ramakant 
int main(int argc, char* argv[])
{

}
'''
