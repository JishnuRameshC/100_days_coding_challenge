def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(2,3,4,5,6))

def calculate(a,**kwargs):
    a += kwargs['sum']
    a *= kwargs["mult"]
    print(a)

calculate(sum=10, mult= 10, a= 0)


class Car:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.brand = kwargs.get("brand")

car = Car(name= "skj", brand = "gtr")
print(car.name)
