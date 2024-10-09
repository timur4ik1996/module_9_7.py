def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        for i in range(2, num):
            if num % i == 0:
                print("составное")
                break
        else:
            print("простое")
    return wrapper

@ is_prime
def sum_three(*nambers):
    print(sum(nambers))
    return sum(nambers)


sum_three(2, 3, 6)

