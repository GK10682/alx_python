#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")




    #!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number >=0:
    print("{} is positive".format(number))
elif number==0:
    print("{} is 0".format(number))
else:
   print("{} is negative".format(number))