from __future__ import print_function
import random
try: from six.moves import input
except ImportError: pass
print("1.Generate random number\n2.Name/Number Selector\n3.Quit")
decision = int(input("Input:"))
if decision == 1:
        min = int(input("Min Number:"))
        max = int(input("Max Number:"))
        randomized = random.randint(min, max)
        print ("Random generated number:", randomized)
elif decision == 2:
        name = input("Seperate the names/numbers by a comma and space\nNames/Numbers:")
        names = name.replace(',', '').split()
        final = random.choice(names)
        print (final)
elif decision == 3:
        quit()
else:
        print ("Incorrect Choice")
        quit()
