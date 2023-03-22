#morgenne
def decode(encoded_password):
    #will implement functionality later
    pass

def encode(original_password):
    encoded = ""
    for i in original_password:
        encoded += str((int(i)+3)%10)
    return encoded

loop=True
while loop== True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        code = password
        print("Your password has been encoded and stored!")
        new_password = encode(code)

    elif option == 2:
        decoded_password = decode(new_password)
        print(f"The encoded password is {new_password}, and the original password is {decoded_password}.")

    elif option == 3:
        loop = False
        break
