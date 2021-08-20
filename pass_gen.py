# password Generator
import random


def pass_gen(n):
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sc = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    spec_char = '!@#$%^&*()_-\"''"'
    all = uc+sc+num+spec_char
    # if length is not specified -- default length of password is taken as 8
    if n == 0:
        password = ''.join(random.sample(all, 8))
    # if length is specified  --length of password is n
    else:
        password = ''.join(random.sample(all, n))
    return password


# Driver Code
n = int(input("Enter Length of password:(----0 if you don't have specific length----)\n"))
print(pass_gen(n))
