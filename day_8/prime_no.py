def prime_checker(number):
    prime = True
    for num in range(2, number):
        if number % num == 0:
            prime = False
    if prime:   
        print(f'{number} is prime')
    else:
        print(f"{number} not a prime")

n = int(input("enter a number : "))
prime_checker(n)
