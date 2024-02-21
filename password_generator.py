import random as rd

x = int(input("enter the lenght of the password you want: "))
alpha = "abcdefghijklemnopqrstvwxyz0123456789/.,><'\":;\\}]{[=+_-)(*&^%$#@!`~)"

i = 0
for i in range(x):
    password = rd.choice(alpha)
    i += 1
    print(password, end="")
     