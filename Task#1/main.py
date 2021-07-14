import pytest

import Buh_app


class TestBuhApp:

    def test_people(self):
        # Проверит первые 10 документов
        for doc in Buh_app.documents[0:11]:
            numb = doc["number"]
            fio = doc["name"]

            # print('\n', numb, '=', fio)

            assert Buh_app.p_people(numb) == fio

    def test_shelf(self):
        # Введёт номера первых 10 документов
        for doc in Buh_app.documents[0:11]:
            numb = doc["number"]
            for numb_shelf, doc in Buh_app.directories.items():
                if numb in doc:

                    # print(f'\nДокумент {numb} ===> № Полки {numb_shelf}:{doc}')

                    assert Buh_app.s_shelf(numb) == numb_shelf

    def test_list_all_doc(self):
        result = ''
        for dct1 in Buh_app.documents:
            result += f'- {" ".join(dct1.values())}.\n'
        assert Buh_app.l_list_all_doc() == result

    @pytest.mark.parametrize('type_doc, numb_doc, fio, number_shelf', [
        ('passport', '11 22 123456', 'Pop It Ivanovich', 1),
        ('visa', '344 765', 'Ronaldo Prostorovich', 2),
        ('SSN', '33 22 4444', 'Borack Obama', 3),
        ('DL', '123 456 789', 'Evgeniy Taran', 3)])
    def test_add_doc(self, type_doc, numb_doc, fio, number_shelf):
        Buh_app.a_add(type_doc, numb_doc, fio, number_shelf)
        res_added = False
        res_added_shelf = False

        for doc in Buh_app.documents:
            test_string = {'type': type_doc, 'number': numb_doc, 'name': fio}
            if doc == test_string:
                res_added = True

        for shelf, doc_in_shelf in Buh_app.directories.items():
            if numb_doc in doc_in_shelf and number_shelf == int(shelf):
                res_added_shelf = True
        assert res_added is True and res_added_shelf is True

    def test_del_doc(self):
        # Введёт номера первых 10 документов, и проверит удалена ли запись из данных
        # print()
        # print(Buh_app.documents)
        # print(Buh_app.directories)
        result_in_documents = False
        result_in_directories = False
        for numb_index, doc in enumerate(Buh_app.documents[0:11]):  # Для проверки [0:1]
            test_string = {'type': doc['type'], 'number': doc['number'], 'name': doc['name']}
            Buh_app.d_delete(doc['number'])
            for doc_search in Buh_app.documents[0:11]:  # Для проверки [0:1]
                if doc_search == test_string:
                    result_in_documents = True
            for shelf, doc_in_shelf in Buh_app.directories.items():
                if doc['number'] in doc_in_shelf:
                    result_in_directories = True
            assert result_in_documents is False and result_in_directories is False
        # print()
        # print(Buh_app.documents)
        # print(Buh_app.directories)
