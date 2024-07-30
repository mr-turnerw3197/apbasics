# Ask the user for width and loop until they
# enter a number that is more than zero

error = "ENTER A NUMBER MORE THAN ZERO, OR ELSE"
while True:

    try:
        # Ask the user for a number
        width = float(input("width: "))

# check that the number is more than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)