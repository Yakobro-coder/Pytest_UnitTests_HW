import requests


class YandexDrive:
    def __init__(self, token):
        self.token = token
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, name_folder):
        self.name_folder = name_folder
        # Создаем папку для хранения ФОТО
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.name_folder}
        response = requests.put(url, headers=self.headers, params=params)
        if response.json().get('message') is not None:
            print(response.json().get('message'))

        return response.status_code

    def search_folder(self, name_folder):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': name_folder}
        response = requests.get(url, headers=self.headers, params=params)
        print(response.status_code)
        return response.status_code
