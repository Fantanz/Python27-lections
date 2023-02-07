print("Введите пароль :")
password =input()

if len(password)>=8 and password.isalpha()==False and password.isdigit()==False:
    print("Ваш пароль сохранен")
else:
    print('asdad')