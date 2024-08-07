def num_check(question):

    error = "ENTER A NUMBER MORE THAN ZERO, OR ELSE\n"
    while True:

        try:
            # Ask the user for a number
            response = float(input(question))

    # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine starts here...


keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost / m: ")

    # Calculate perimeter and price for the fence
    perimeter = (width + height) * 2
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price. ${price:.2f}")

    # Ask the user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

    print("Thank you for using the area / perimeter calculator")
