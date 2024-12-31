#How many times does a user want a cat to meow?

#Ask user how many times
def main():
    number = get_number()
    meower(number)

#ask user for their number of meows

def get_number():
    while True:
        n = int(input("How many meows you want? "))
        if n > 0:
            return n

#print the user input that many times
def meower(n):
    for _ in range (n):
        print("MEOW!")

main()