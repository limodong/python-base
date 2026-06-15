class Dog:
    def __init__(self):
        print("。。。。init。。。。")

    def __call__(self,*args):
        sum = 0
        for i in args:
            sum += i
        print("------call------",sum)

    classmethod
    def speak():
        print("speak。。。。")
    
d = Dog()
type(d).__call__(d,1,2,3,4,5,6,7)
Dog.speak()
type(Dog.speak).__call__(Dog.speak)
d(1,2,3)
def sum(x,y):
    return x+y
print(type(sum).__call__(sum,1,2))

def speak(str):
    print(str)
A = type.__call__(type,"A",(),{"name":"111","speak":"speak"})
print(A)
a = A()
print(a.speak)
