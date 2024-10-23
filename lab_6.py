# Daniel Green

def encode(password):
    # must be string
    arr = ''
    for i in password:
        arr = arr + str((int(i) + 3) % 10)
    return arr

def decode(encrypted):
    arr = ''
    for i in encrypted:
        arr = arr + str((int(i) - 3) % 10)
    return arr

def main():
    while True:
        op = input(f'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

        if op == '1':
            en = encode(input('Please enter your password to encode: '))
            print("Your password has been encoded and stored!")

        elif op == '2':
            print(f'The encoded password is {en}, and the original password is {decode(en)}.')

        elif op == '3':
            break


if __name__ == '__main__':
    main()
