documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def vvod():
    helper = '''
                                 Помощник по документообороту v1.0
                 Данная программа помощник для реализации ведения и хранения документов. 
            Программа напомнит вам какой документ кому принадлежит, и на какой полке он хранится.

                              Программа осуществляет следующие функции:
    p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l – команда, которая выведет список всех документов в формате "passport 2207 876234 Василий Андреевич";
    sh - команда, котрая выведет количество полок, и какие документы на ней хранятся.
    a – команда, которая добавит новый документ в каталог и в перечень полок, спросив номер документа, тип,
    имя владельца и номер полки, на котором он будет храниться;
    d – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – команда, которая спросит номер новой полки и добавит ее в перечень.

    exit - Команда для выхода из программы.
    help - что бы посмотреть перечень команд.

    Внимание: p, s, l, sh, a, d, m, as, exit, help - это команды, которы вам надо вветси.
    Пример: Вы хотите узнать по номеру документа, кому пренадлежит документ(это команда p).
    Вам необходимо ввести команду в поле ввода. "Введите команду: p"; 
    '''
    print(helper)
    command_enter = True
    while command_enter:
        command = input('\nВведите команду: ')

        if command == 'p':
            insert = input('Введите номер документа: ')
            res = p_people(insert)
            if len(res) != 52:
                print(f'Документ на имя:', res)
            else:
                print(res)

        elif command == 's':
            insert = input('Введите номер документа: ')
            res = s_shelf(insert)
            if len(res) != 65:
                print(f'Полка номер: {res}')
            else:
                print(res)

        elif command == 'l':
            print(l_list_all_doc())

        elif command == 'sh':
            print(sh_directories())

        elif command == 'a':
            type_doc = input('ВВедите тип документа: ')
            numb_doc = input('ВВедите номер документа: ')
            fio = input('ВВедите ФИО владельца документов: ')
            print(a_add(type_doc, numb_doc, fio))

        elif command == 'd':
            insert = input('Введите номер документа для его удаления: ')
            print(d_delete(insert))

        elif command == 'm':
            print(m_move())

        elif command == 'as':
            print(as_add_shelf())

        elif command == 'help':
            print(helper[261:1261:])

        elif command == 'exit':
            command_enter = False

        else:
            print('Вы ввели не верную команду. Напишите команду help что бы ознакомиться со спсиком команд.')


def p_people(insert):
    """
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.
    """
    while True:
        for dct1 in documents:
            if dct1['number'] == insert:
                return dct1["name"]

        return 'Такой документ не найден. Проверьте номер документа.'


def s_shelf(insert):
    while True:
        for key, val in directories.items():
            if insert in val:
                return key
        return 'Такой документ не найден. Проверьте номер документа.'


def l_list_all_doc():
    result = ''
    for dct1 in documents:
        result += f'- {" ".join(dct1.values())}.\n'
    return result


def sh_directories():
    result = ''
    for key, val in directories.items():
        result += f'Полка {key} с документами: {val}\n'
    return result


def a_add(type_doc, numb_doc, fio, number_shelf=0):
    new_doc = {'type': type_doc, 'number': numb_doc, 'name': fio}

    while number_shelf == 0:
        number_shelf = input('Документ добавлен в каталог. На какой полке он будет хранится: ')
        if number_shelf.isdigit():
            number_shelf = int(number_shelf)
            if number_shelf < 0 or number_shelf > len(directories):
                print(f'Полки с номером "{number_shelf}", не существует. Введите номер полки корректно.')
                print(f'На данный момент у вас {len(directories)} полки.')
                number_shelf = 0
        else:
            print(f'Полки с номером "{number_shelf}", не существует. Введите номер полки корректно.')
            number_shelf = 0

    documents.append(new_doc)
    directories[str(number_shelf)].append(new_doc['number'])
    return f'Документ "{" ".join(new_doc.values())}" добавлен и хранится на полке №{number_shelf}.'


def d_delete(insert):
    res = ''
    while True:
        if insert == '-1':
            break
        else:
            for number, dct_doc in enumerate(list(documents)):
                if dct_doc['number'] == insert:
                    res = f'Документ "{" ".join(dct_doc.values())}" удален из каталога и с полки хранения №'
                    del (documents[number])

                    for key, val in list(directories.items()):
                        for number_position, number_doc in enumerate(val):
                            if number_doc == insert:
                                res += f'{key}.'
                                del (directories[key][number_position])
                                return res
            print('Такой документ не найден. Проверьте номер документа. Для выхода введите: -1')
            insert = input('Введите номер документа для его удаления: ')


def m_move():
    true_doc = True
    true_shelf = False
    error = 0
    while true_doc:
        b = input('Введите номер документа: ')
        for key, val in list(directories.items()):
            for number_position, number_doc in enumerate(val):
                error += 1
                if number_doc == b and true_shelf == False and true_doc == True:
                    print(f'Документ  №{number_doc} найден на полке №{key}')
                    del (directories[key][number_position])
                    true_shelf = True
                    true_doc = False
                if len(directories) == error and true_doc == True:
                    print('Такой документ не найден. Проверьте номер документа.')
                    error = 0
                while true_shelf:
                    number_shelf = int(input('Введите номер полки, куда переместить документ: '))
                    if number_shelf <= len(directories):
                        directories[str(number_shelf)].append(number_doc)
                        print(f'Документ {number_doc} перенесён на полку {number_shelf}.')
                        true_shelf = False
                    else:
                        print(f'Полки с номером {number_shelf} не существует. '
                              f'\nУ вас от 1 до {len(directories)} полок. Выбирите одну их них.')


def as_add_shelf():
    true_test = True
    print(f'На данный момент количетсова ваших полок: {len(directories)} шт.')
    while true_test:
        add_shelf = input('Хотите добавть ещё одну полку?(ДА введите +; НЕТ -) Ввод: ')
        if add_shelf == '+':
            directories.setdefault(str(len(directories) + 1), [])
            print(f'{len(directories)}-я полка добавлена.')
            true_test = False
        elif add_shelf == "-":
            true_test = False
            pass
        else:
            print('Вы ввели что то кроме + или -. Определитесь :)')


if __name__ == '__main__':
    vvod()
