def genInfo():
    print("and whats your age?")
    age = str(input())
    if age != "":
        print("you are " + {age} + "years old")
        gender = input("please input your gender:")
        print("so you are " + __name__ + ". and you are" + gender + ".and your age is" + age + "?")
    else:
        print("stop screwing around and input a number")
        genInfo()

def start():
    n = input("Enter your name: ")
    if n != "":
        print("hello " + n)
        genInfo()
    else:
        print("give a name please")
        start()

start()
