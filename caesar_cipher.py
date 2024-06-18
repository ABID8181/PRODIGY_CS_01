def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift if not decrypt else -shift
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    # Input message and shift value from user
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (a positive integer): "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_cipher(encrypted_message, shift, decrypt=True)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
