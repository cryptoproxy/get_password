

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

get_pwd('private_zabugor_40000.txt')

