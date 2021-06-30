import requests
from pprint import pprint
TOKEN = ''

class YaDisk:
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return {
            'Authorization': f'OAuth {TOKEN}',
            'Content-Type': 'application/json'
            }
    def get_files_list(self):
        headers = self.get_headers()
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        response = requests.get(file_url, headers=headers)
        response.raise_for_status
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params )
        response.raise_for_status
        pprint(response.json())
        return response.json()
    
    def upload_file_to_disk(self, disk_file_path, file_name):
        href = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status
        if response.status_code == 201:
            print('Загружено')



if __name__ == "__main__":  
    ya = YaDisk(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path='client.txt/', file_name='test.txt')


