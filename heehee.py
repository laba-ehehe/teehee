def encode(password):
    encode = ''
    for char in password:
        encoded_char = chr(ord(char) + 1)
        encode += encoded_char
    return encode


def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        choice = int(input('Please enter an option: '))
        if choice == 3:
            break
        else:
            password = input('Please enter your password to encode: ')
            if choice == 1:
                encode = encode(password)
                print('Your password has been encoded and stored!')
            elif choice == 2:
                print(f'The encoded password is {encode}, and the original password is {password}.')

if __name__ == '__main__':
    main()
