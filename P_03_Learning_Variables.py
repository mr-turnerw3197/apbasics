# ask the user for their name
username = input("What is your name!? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number!? "))

# Double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num  * fav_num

# Greet the user
print(f"HI {username}, your favourite number is {fav_num}")

# Output the results of doubling, halving and
# squaring their favourite integer
print(f"your favourite number doubled is {double}")
print(f"your favourite number halved is {halve}")
print(f"your favourite number squared is {square}")
print("have a tremendous day!!")