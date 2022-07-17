def prime_checker(number):
    if number <= 1:
        print("It's not a prime number.")
    else:
        c = 0
        for i in range(2, round(number/2) + 1):
            if number % i == 0:
                c += 1
                if c == 1:
                    print("It's not a prime number.")
                    break
        if c==0:
            print("It's a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)
