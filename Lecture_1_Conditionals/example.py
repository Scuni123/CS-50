#main function
def main():
    user_name = name()
    number = pick_num()
    real_num = number - 1
    team = find_team(real_num)
    print(f"Hello, {user_name}, you chose lucky number {number}. Your new favorite PL team is {team}!")

#Ask for their first and last name then say hello to first name
def name():
    name = input("What is your first and last name? ")
    return name

#Ask for a number and print out list comparing PL teams
def pick_num():
    while True:
        try:
            n = (int(input("Pick a number 1-3. ")))
            if 0 < n < 4:
                return n
            else:
                print("This number is not between 1-3. ")
        except ValueError:
            print("Opps! Not a number. Try again.")

def find_team(number):
    pl_teams = ["Chelsea", "ManU", "Liverpool"]
    team = pl_teams[number]
    return team

#run main file and check for module use
if __name__ == "__main__":
    main()