def main():
    col_count=int(input("How many columns do you want? "))
    pwr_up = int(input("How many power up blocks? "))
    block_h= int(input("Let's creat a block. How heigh should it be? "))
    block_w= int(input("How wide is the block? "))
    print_column(col_count)
    power_up(pwr_up)
    block(block_w, block_h)

def print_column (height):
    for _ in range(height):
        print("#")

def power_up(length):
    print("?" * length)

def block(width, height):
    for _ in range(height):
        print("x" * width)

main()