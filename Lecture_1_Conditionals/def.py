def main():
    name = input ("What is your Name? ").strip().title()
    hello(name)

def hello(to="world"): 
    print ("Hello,", to)

main()