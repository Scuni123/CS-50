def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

#this checks to see if the program was run from the command line. Otherwise wont run so when
#you would call a function in another program, main isn't run
if __name__ == "__main__":
    main()