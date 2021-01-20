shift = 3

def ceaser_cypher_encoder(text_to_encrypt):
    """Ceaser Cypher Encoder for text messages"""

    original_characters = list(text_to_encrypt)
    encrypted_characters = []
    global shift

    # Encrypt message:
    for i in range(len(original_characters)):
        original_ascii = ord(original_characters[i])
        encrypted_ascii = (original_ascii + shift) % 127

        encrypted_character = chr(encrypted_ascii)
        encrypted_characters.append(encrypted_character)

    encrypted_text = "".join(encrypted_characters)
    return encrypted_text

def ceaser_cypher_decoder(hash_to_decode):
    """Ceaser Cypher Encoder for text messages"""
    encrypted_characters = list(hash_to_decode)
    original_characters = []
    global shift

    # Decode message:
    for i in range(len(encrypted_characters)):
        encrypted_ascii = ord(encrypted_characters[i])
        original_ascii = (encrypted_ascii - shift) % 127

        original_character = chr(original_ascii)
        original_characters.append(original_character)

    original_text = "".join(original_characters)
    return original_text
