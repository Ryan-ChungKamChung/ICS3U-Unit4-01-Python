#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program adds numbers up to the inputted number


def main():
    # Function adds numbers up to the inputted number

    print("Give me a positive number and I will add numbers up"
          " until the number you input")

    # Input
    number_string = input("Enter number: ")

    # Process
    try:
        number = int(number_string)

        # https://stackoverflow.com/questions/34244588/
        # reject-negative-numbers-as-exceptions-in-python
        assert number > 0

        loop_counter = 0
        number_sum = 0

        while loop_counter < number:
            loop_counter = loop_counter + 1
            number_sum = number_sum + loop_counter

        # Output
        print(number_sum)

        # https://stackoverflow.com/questions/34244588/
        # reject-negative-numbers-as-exceptions-in-python
    except AssertionError:
        # Output
        print("This isn't a valid number")
    except Exception:
        # Output
        print("This isn't a valid number")


if __name__ == "__main__":
    main()
