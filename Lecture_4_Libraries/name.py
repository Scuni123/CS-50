import sys

if len(sys.argv) < 2:
    print("Too short ")
elif len(sys.argv) > 2:
    print("Too long")
else:
    print("Hello, my name is", sys.argv[1])