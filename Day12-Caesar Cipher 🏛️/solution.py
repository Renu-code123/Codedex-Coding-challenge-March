##
def decode_message(message, shift):
    decoded = ""
    
    for char in message:
        if char == " ":
            decoded += " "
        else:
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decoded += new_char
    
    return decoded
