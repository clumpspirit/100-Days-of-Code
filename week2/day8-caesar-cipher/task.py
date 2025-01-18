import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    new_text = ""

    # Return the inverse of the new_index below
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Sort through each letter in message
    for letter in original_text:

        # If there are spaces in the message
        if letter not in alphabet:
            new_text += letter

        else:
            # Create new index
            index = alphabet.index(letter)
            new_index = index + shift_amount

            # Get the remainder of n index / 25. This is to keep the index within range of the list.
            new_index %= len(alphabet)

            # Create shifted output using new index
            new_letter = alphabet[new_index]
            new_text += new_letter

    print(f"\n{encode_or_decode}d result: {new_text}")


# Loop session
session = "Y"
while session == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    session = input("Again? (Y/n)\n").upper()
