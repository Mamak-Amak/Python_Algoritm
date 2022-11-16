"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


 '''Вариант№ 1'''

Users = {'Alabamag43@gmail.com': {"password": '142745rtrt',
                                   "activated": False},
         'Fromashes444@gmail.com': {"password": '54634dfdfe',
                                     "activated": True},
         'Antanta56@gmail.com': {"password": 'passs4444',
                                      "activated": False}}


def authorisation_1(login: str, password: str):
    if login in users.keys():
        if  password in users[login].values():
            if users [login] ['activated']:
                print ("Complete")

                return True

            else:
                print ("Вам нужно активировать свой аккаунт, пожалуйста, следуйте инструкции..") # O(1)
                return False

        else:
            print ("Неверный пароль")

            return False

    else:
        print ("Такого пользователя не существует")

        return False


'''
сложность: O(n ^ 2)
линейное
'''

'''Вариант№ 2'''

def authorisation_2(login: str, password: str):

    user_exists = False

    for user in users.keys():
        if password == login:
            user_exists = True
        break

    if user_exists:
        password_correct = users[login]['password'] == password
        activated = users[login]['activated']
        if password_correct:
            if activated:
                print("Доступ разрешен")
                return True
            else:
                print("Вам нужно активировать свой аккаунт, пожалуйста, следуйте инструкции..")
                return False
        else:
            print("Невверный пароль")
            return False
    else:
        print("Пользователь не существует")
        return False

'''
Сложность алгоритма O(n) : линейное
'''
