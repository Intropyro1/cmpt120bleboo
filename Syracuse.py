#Syracuse sequence
#   program returns syracuse sequence
#

def syr(x):
    if x == 1:
        print("1")
        return
    while x != 1:
        if x % 2 == 0:
            x /= 2
            print(x)
        else:
            x = 3*x+1
            print(x)
def main():
    x = int(input("Enter a number: "))
    syr(x)

main()
