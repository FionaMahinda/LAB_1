# This program inputs 5 numbers from the user and finds the sum of numbers

def main():
    n = int(input("Enter number: "))
    sum = 0
    # loop from 1 to n
    for num in range(1, n + 1):
        sum = sum + num
    print("Sum of first", n, "numbers is: ", sum)

main()
