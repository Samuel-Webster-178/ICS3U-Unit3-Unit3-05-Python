#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


def main():
    # I calculate circumference

    # input
    month_number = int(input("Enter a number corresponding to a month (1-12): "))

    # process & output
    if month_number == 1:
        print("January")
    elif month_number == 2:
        print("February")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("Invalid Input")

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
