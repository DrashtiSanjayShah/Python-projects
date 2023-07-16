a = int(input("enter the number to be checked: "))
if (a==1):
    print(a,'is neither prime nor composite')

if (a>1):
    is_prime = True
    for i in range(2, int(a/2)+1):
        if (a%i == 0):
            is_prime = False
            break
    if is_prime:
        print(a, 'is prime')
    else:
        print(a, 'is not prime')
else:
    print('enter a number greater than 1')
