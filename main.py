run = True
print("This encryption tool uses ROT13 system so it only encrypts alphabet letters, any other symbol will not be encrypted")
def encrypt():
    message = input("Input the message to encode: ").lower()
    encrypted_message = ""
    for i in range(len(message)):
        new_num = ord(message[i])
        if new_num == 32:
            encrypted_message += chr(new_num)
        elif new_num < 97 or new_num > 122:
            encrypted_message += "?"
        elif (new_num + 13) > 122:
            encrypted_message += chr(new_num - 13)
        else:
            encrypted_message += chr(new_num + 13)

    print("Encrypted message: " + encrypted_message)

def decrypt():
    message = input("Input the message to encode: ").lower()
    decrypted_message = ""
    for i in range(len(message)):
        new_num = ord(message[i])
        if new_num == 32:
            decrypted_message += chr(new_num)
        elif new_num < 97 or new_num > 122:
            decrypted_message += "?"
        elif (new_num - 13) < 97:
            decrypted_message += chr(new_num + 13)
        else:
            decrypted_message += chr(new_num - 13)

    print("Decrypted message: " + decrypted_message)


while run == True:
    print("Action:  1-Encrypt  2-Decrypt  3-Exit")
    script_action = int(input())

    if script_action == 1:
        encrypt()
    elif script_action == 2:
        decrypt()
    elif script_action == 3:
        run = False
