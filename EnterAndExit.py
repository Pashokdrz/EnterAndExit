key=input('Чтобы программа заработала введите 1: ')
key=int(key)
i=0
rangeOfConnect=1
reg=[]
connect=[['Admin', 'admin112', 'admin'], ['User', '777user1', 'user']]
password=('qwerty1')
def changeNickname():
    import os
    os.system('cls')
    person=input('Введите новый nickname: ')
    key1=1
    key2=1
    while key1==1:
        u=0
        control=0
        while key2==1 and u<len(connect):
            if person==connect[u][0]:
                import os
                os.system('cls')
                person=input('Nickname уже занят, придумайте другой: ')
                key2=0
                control=1
            u=u+1
        key2=1
        if control==0 and u==len(connect):
            key1=0
    connect[i][0]=person
    print('Nickname успешно изменен')
    qq=input('Нажмите Enter для возврата в меню: ')
def changePass():
    import os
    os.system('cls')
    passwordControl=input('Введите ваш действующий пароль: ')
    if passwordControl==connect[i][1]:
        connect[i][1]=input('Введите новый пароль: ')
        b=connect[i][1]
        print('Пароль успешно изменен')
    else:
        print('Пароль введён неверно')
    qq=input('Нажмите Enter для возврата в меню: ')
while key==1:
    key1=1
    key2=1
    control=0
    import os
    os.system('cls')
    print('1.Вход')
    print('2.Регистрация')
    print('3.Выход')
    z=input()
    z=int(z)
    if z==3:
        key=0
    if z==1:
        import os
        os.system('cls')
        b=input('Введите ваш логин: ')
        key1=1
        i=0
        while b!=connect[i][0] and key1==1:
            i=i+1
            if i==len(connect):
                import os
                os.system('cls')
                print('Такого пользователя не зарегестрировано')
                key1=0
                i=0
                qq=input('Нажмите Enter для возврата в меню: ')
        if b==connect[i][0]:
            import os
            os.system('cls')
            b=input('Введите ваш пароль: ')
            while b!=connect[i][1] and key1==1:
                import os
                os.system('cls')
                print('Неверный пароль')
                key1=0
                i=0
                qq=input('Нажмите Enter для возврата в меню: ')
            while rangeOfConnect>0 and b==connect[i][1] and connect[i][2]=='user':
                import os
                os.system('cls')
                print('Добро пожаловать ', connect[i][0],)
                print('Выберите действие:')
                print('1.Сменить пароль')
                print('2.Сменить nickname')
                print('3.Удалить аккаунт')
                print('4.Выход')
                z=input()
                z=int(z)
                if z==4:
                    key1=0
                    b=0
                    i=0
                if z==1:
                    changePass()
                if z==2:
                    changeNickname()
                if z==3:
                    import os
                    os.system('cls')
                    connect.pop(i)
                    key1=0
                    b=('')
                    i=0
                    print('Аккаунт успешно удалён')
                    rangeOfConnect=len(connect)
                    qq=input('Нажмите Enter для возврата в меню: ')
            while rangeOfConnect>0 and b==connect[i][1] and connect[i][2]=='admin':
                import os
                os.system('cls')
                print('Добро пожаловать ', connect[i][0],)
                print('Выберите действие:')
                print('1.Сменить пароль')
                print('2.Сменить nickname')
                print('3.Удалить аккаунт')
                print('4.Создать аккаунт')
                print('5.Изменить пароль пользователю')
                print('6.Сбросить пароль пользователю')
                print('7.Список пользователей')
                print('8.Изменить роль пользователя')
                print('9.Выход')
                z=input()
                z=int(z)
                if z==8:
                    import os
                    os.system('cls')
                    person=input('Введите nickname пользователя, которому хотите изменить роль: ')
                    key1=1
                    u=0
                    while person!=connect[u][0] and key1==1:
                        u=u+1
                        if u==len(connect):
                            import os
                            os.system('cls')
                            print('Такого пользователя не зарегестрировано')
                            key1=0
                            u=0
                            qq=input('Нажмите Enter для возврата в меню: ')
                    if person==connect[u][0]:
                        import os
                        os.system('cls')
                        b2=input('Выберите роль пользователя: 1-админ, 2-юзер: ')
                        b2=int(b2)
                        if b2==1:
                            connect[u][2]=('admin')
                        if b2==2:
                            connect[u][2]=('user')
                if z==7:
                    import os
                    os.system('cls')
                    print('Вот список всех пользователей: ')
                    print(connect)
                    qq=input('Нажмите Enter для возврата в меню: ')
                if z==5:
                    import os
                    os.system('cls')
                    person=input('Введите nickname пользователя, которому хотите поменять пароль: ')
                    key1=1
                    u=0
                    while person!=connect[u][0] and key1==1:
                        u=u+1
                        if u==len(connect):
                            import os
                            os.system('cls')
                            print('Такого пользователя не зарегестрировано')
                            key1=0
                            u=0
                            qq=input('Нажмите Enter для возврата в меню: ')
                    if person==connect[u][0]:
                        import os
                        os.system('cls')
                        connect[u][1]=input('Введите новый пароль: ')
                        print('Пароль успешно изменен')
                        qq=input('Нажмите Enter для возврата в меню: ')
                if z==6:
                    import os
                    os.system('cls')
                    person=input('Введите nickname пользователя, которому хотите сбросить пароль: ')
                    key1=1
                    u=0
                    while person!=connect[u][0] and key1==1:
                        u=u+1
                        if u==len(connect):
                            import os
                            os.system('cls')
                            print('Такого пользователя не зарегестрировано')
                            key1=0
                            u=0
                        if person==connect[u][0]:
                            connect[u][1]=password
                            print('Пароль успешно изменен')
                            qq=input('Нажмите Enter для возврата в меню: ')
                if z==4:
                    import os
                    os.system('cls')
                    person=input('Придумайте пользователю nickname: ')
                    key1=1
                    key2=1
                    while key1==1:
                        u=0
                        control=0
                        while key2==1 and u<len(connect):
                            if person==connect[u][0]:
                                import os
                                os.system('cls')
                                person=input('Nickname уже занят, придумайте другой: ')
                                key2=0
                                control=1
                            u=u+1
                        key2=1
                        if control==0 and u==len(connect):
                            key1=0
                    reg.append(person)
                    reg.append(password)
                    import os
                    os.system('cls')
                    b2=input('Выберите роль пользователя: 1-админ, 2-юзер: ')
                    b2=int(b2)
                    if b2==1:
                        reg.append('admin')
                    if b2==2:
                        reg.append('user')
                    connect.append(reg)
                    reg=[]
                if z==9:
                    key1=0
                    b=0
                if z==1:
                    changePass()
                if z==2:
                    changeNickname()
                if z==3:
                    import os
                    os.system('cls')
                    t=input('Какой аккаунт удалить?(1-свой, 2-пользователя): ')
                    t=int(t)
                    if t==1:
                        connect.pop(i)
                        key1=0
                        i=0
                        b=0
                        print('Аккаунт успешно удалён')
                        qq=input('Нажмите Enter для возврата в меню: ')
                    if t==2:
                        import os
                        os.system('cls')
                        person=input('Введите nickname пользователя, которого хотите удалить: ')
                        key1=1
                        u=0
                        while person!=connect[u][0] and key1==1:
                            u=u+1
                            if u==len(connect):
                                import os
                                os.system('cls')
                                print('Такого пользователя не зарегестрировано')
                                key1=0
                                u=0
                        if person==connect[u][0]:
                            connect.pop(u)
                            print('Аккаунт успешно удалён')
                            qq=input('Нажмите Enter для возврата в меню: ')
                    rangeOfConnect=len(connect)

    if z==2:
        import os
        os.system('cls')
        b=input('Придумайте себе nickname: ')
        key1=1
        key2=1
        while key1==1:
            i=0
            control=0
            while key2==1 and i<len(connect):
                if b==connect[i][0]:
                    import os
                    os.system('cls')
                    b=input('Nickname уже занят, придумайте другой: ')
                    key2=0
                    control=1
                i=i+1
            key2=1
            if control==0 and i==len(connect):
                key1=0
        import os
        os.system('cls')
        b1=input('Придумайте пароль: ')
        reg.append(b)
        reg.append(b1)
        reg.append('user')
        connect.append(reg)
        reg=[]
