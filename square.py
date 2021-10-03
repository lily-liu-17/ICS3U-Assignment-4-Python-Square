#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program will show whether or not the rectangle is a square


def main():
    # This program will show whether or not the rectangle is a square
    # Input
    length = input("Enter the length of a rectangle (cm) : ")
    width = input("Enter the length of a rectangle (cm) : ")

    # Process and Output
    try:
        length = int(length)
        width = int(width)
        if length == width:
            print("This rectangle is a square.")
            print("")
        else:
            print("This rectangle is not a square.")
    except Exception:
        print("Invalid input")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
