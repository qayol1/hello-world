import sys

def greeting (text = "Hello World!" , endsign = "\n"):
    print(text , end = endsign)

def argument (position):
    return sys.argv[position]

length = len(sys.argv)

if length < 2:
    greeting()
else:
    greeting("Hello ", endsign = "")
    for i in range(length):
        if i > 0 and i < length-1 :
            greeting(argument(i), endsign = " ")
        if i == length - 1 :
            greeting(argument(i) + "!")