# Ask the user for width and loop until they
# enter a number that is more than zero
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

# Main Routine goes Here
# Check Weight
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()
# check Height
for item in range(0, 2):
     height = num_check("Height: ")
     print(height)