import pytest
import Yandexdrive

TOKEN = 'insert_token_yandex_disk'


class TestYandex:

    def setup_class(self):
        self.test = Yandexdrive.YandexDrive(TOKEN)

    @pytest.mark.parametrize('name_folder, result', [('Test_Folder', 201),
                                                     ('Test_Search_Folder', 201),
                                                     ('Test_Folder', 409),
                                                     ('Test_FolderTest_FolderTest_FolderTest_FolderTest_Folder'
                                                      'Test_FolderTest_FolderTest_FolderTest_FolderTest_Folder'
                                                      'Test_FolderTest_FolderTest_FolderTest_FolderTest_Folder'
                                                      'Test_FolderTest_FolderTest_FolderTest_FolderTest_Folder'
                                                      'Test_FolderTest_FolderTest_FolderTes', 404)])
    def test_create_folder(self, name_folder, result):
        assert self.test.create_folder(name_folder) == result

    @pytest.mark.parametrize('name_folder, result', [('Test_Search_Folder', 200),
                                                     ('Test_Search_Folder2', 404)])
    def test_search_folder(self, name_folder, result):
        assert self.test.search_folder(name_folder) == result
