from art import logo
print(logo)

status = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode_message(message, shift):
    encoded_message = ""
    for x in message:
        if x in alphabet:
            position = alphabet.index(x)
            position += shift
            if position > 25:
                position %= 26
            encoded_message += alphabet[position]
        else:
            encoded_message += x
    print(f"Here's the encoded result: {encoded_message}")


def decode_message(message, shift):
    decoded_message = ""
    for x in message:
        if x in alphabet:
            position = alphabet.index(x)
            position -= shift
            if position < 0:
                position %= 26
            decoded_message += alphabet[position]
        else:
            decoded_message += x
    print(f"Here's the decoded result: {decoded_message}")


while status:
    user_input = input("Type 'encode' or 'e' to encrypt, type 'decode' or 'd' to decrypt:\n").lower()
    if user_input not in ('encode', 'decode', 'e', 'd'):
        status = False
    else:
        input_message = input("Type your message: \n").lower()
        text_shift = int(input("Type the shift number: \n"))
        if user_input in ('encode', 'e'):
            encode_message(message=input_message, shift=text_shift)
        elif user_input in ('decode', 'd'):
            decode_message(message=input_message, shift=text_shift)
        check_status = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if check_status in ('yes', 'y'):
            status = True
        else:
            status = False
