# для этого нам нужен .txt файл с базой типа login:pass или url:login:pass
# это полезно для создания собственного словаря для брутфорса


def get_pwd(dir):
    with open(dir, 'r', encoding='utf8') as file:
        for line in file:
            try:
                login, password = line.split(':')
                with open('passwords.txt', 'a', encoding='utf8') as file:
                    file.write(password)
            except:
                try:
                    url, login, password = line.split(':')
                    with open('passwords.txt', 'a', encoding='utf8') as file:
                        file.write(password)
                except Exception as ex:
                    print(ex)

get_pwd('file.txt')

