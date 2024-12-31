#while true is very common and standard for user input to make sure they get something right
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow! ")