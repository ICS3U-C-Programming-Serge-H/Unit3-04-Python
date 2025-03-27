# Created by: Serge Hamouche
# Created on: March 27th, 2025
# This program tells the user if the number they input is positive, negative or zero.

def main():

    try:
        # Ask user to input their number.
        user_number = int(input("Enter a number: "))

        # If number > 0 then its positive, if not then its negative,
        # and if the number is 0 then it is just 0.
        if user_number > 0:
            print(" is a positive number.")
        elif user_number < 0:
            print(" is a negative number.")
        else:
            print("is just zero.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
