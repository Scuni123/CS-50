#multiplication. Take the multiples of a num input.
def main():
    number = get_num()
    multi_table(number)

#get a number from a user
def get_num():
    while True:
        try:
            n = int(input("Provide a number for the multiplication table. "))
            return n
        except ValueError:
            print("Not a number. Try again. ")

def multi_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    main()