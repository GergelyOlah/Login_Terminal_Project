#!/usr/bin/env python3

#letter_to_ASCII = ord("A")
#print(type(letter_to_ASCII))
#ASCII_to_letter = chr(65)
#print(ASCII_to_letter)

def ceaser_cypher_encoder():
    """Ceaser Cypher Encoder for text messages"""

    text_to_encrypt = str(input("What do you want to encrypt?\n"))
    original_characters = list(text_to_encrypt)
    encrypted_characters = list()

    shift = int(input("With how many digits do you want to shift the text? (It must be between -127 and 127) \n"))

    # Encrypt message:
    for i in range(len(original_characters)):
        original_ascii = ord(original_characters[i])
        new_ascii = original_ascii + shift

        if 0 <= new_ascii <= 127:
            pass
        elif new_ascii > 127:
            new_ascii = new_ascii - 127 
        else:
            new_ascii = 127 + new_ascii

        new_character = chr(new_ascii)
        encrypted_characters.append(new_character)
        
    encrypted_text = "".join(encrypted_characters)
    
    # Write result to file:
    with open("Ceaser_cypher_ecrypted_message.txt", "w") as f:
        f.write(encrypted_text)
    return print("Message encrypted and written to a file.")

ceaser_cypher_encoder()