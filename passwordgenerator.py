import random

l=int(input("\nENTER THE DESIRED LENGTH OF THE PASSWORD"))
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-++"
p="".join(random.sample(a,l))
print(p)