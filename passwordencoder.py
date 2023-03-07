if __name__ == '__main__':
    menu_status = True
    raw_password = ''
    encoded_pass = ''

    while menu_status:
        print('Menu')
        print('------------')
        print('1. Encode \n2. Decode \n3. Quit \n')

        option = int(input('Please enter an option:'))

        if option == 1:
            raw_password = str(input('Please enter your password to encode:'))

            encoded_pass = ''
            for num in raw_password:
                digit = int(num) + 3
                if digit == 10:
                    digit = 0
                elif digit == 11:
                    digit = 1
                elif digit == 12:
                    digit = 2
                encoded_pass += str(digit)

            print('Your password has been encoded and stored\n')

        elif option == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {raw_password}\n')

        elif option == 3:
            menu_status = False
