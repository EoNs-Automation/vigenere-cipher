def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# Main program loop
while True:
    print("=== Vigenere Cipher ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "3":
        print("Goodbye!")
        break

    if choice not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        continue

    key = input("Enter the passcode: ")
    message = input("Enter the message: ")

    if choice == '1':
        result = encrypt(message, key)
        print("\nEncrypted message:")
        print(result)
    elif choice == '2':
        result = decrypt(message, key)
        print("\nDecrypted message:")
        print(result)
    else:
        print("Invalid choice.")