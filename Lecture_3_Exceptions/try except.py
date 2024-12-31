# Handling errors from users
def main():
#Giving the prompt here to avoid asking for x here and other spots maybe asking for y.
    number = get_num("What's x? ")
    print(f"x is {number}")

def get_num(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("X is not an integer")
            #you can also just use "pass"
        else:
            return x

main()