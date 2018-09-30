password = 'password123'
count = 0
while count < 3:
    userpwd = input('Enter Password:\n')
    count += 1
    if userpwd == password:
        print('Login Successfully, please wait...')
        print('...')
        break
    else :
        print('Password is not correct!')
        print('第',count,'次錯誤')
        if count == 3:
            print('Sorry,you have tried 3 times!')
            break