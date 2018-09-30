## password count to 3
# password = 'password123'
# count = 0
# while count < 3:
#     userpwd = input('Enter Password:\n')
#     count += 1
#     if userpwd == password:
#         print('Login Successfully, please wait.')
#         break
#     else :
#         print('Password is not correct!')
#         print('第', count, '次錯誤')
#         if count == 3:
#             print('Sorry,you have tried 3 times!')
#             break

## password count to 0
password = 'password123'
count = 3
while count > 0:
    userpwd = input('Enter Password:\n')
    count -= 1
    if userpwd == password:
        print('Login Successfully, please wait.')
        break
    else :
        print('Password is not correct!')
        print('WORNING! You still have', count, 'times to try!')
        if count == 0:
            print('Sorry,you have tried 3 times!')
            break


