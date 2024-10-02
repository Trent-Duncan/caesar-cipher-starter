# Trent Duncan
# 10/2/24
# caesar cipher


alphabet= "abcedefghijklmnopqrstuvwxyz"
new_message = ""

user_message = input("Enter your secret message: \n")
key= int(input("Enter a key: \n"))

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position +key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

print("Your new message is" + new_message)