def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.isupper():
                result += chr((shifted - 65) % 26 + 65)
            else:
                result += chr((shifted - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, key):
    return encrypt(text, -key)


def main():
    while True:
        choice = input("Choose an option: \n1. Encrypt\n2. Decrypt\n3. Exit\n")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypted_text = encrypt(text, key)
            print("Encrypted Text:", encrypted_text)

        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypted_text = decrypt(text, key)
            print("Decrypted Text:", decrypted_text)

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please choose again.\n")


if __name__ == "__main__":
    main()
