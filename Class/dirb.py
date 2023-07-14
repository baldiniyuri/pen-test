import requests


class DirbApache:
    def __init__(self, target_url:str) -> None:
        self.target_url = target_url
        self.common_paths = ["/admin/","/login/","/backup/", "/config/", "/wp-admin/", "/phpmyadmin/", "/uploads/"]
        self.founded_paths = []


    def get_paths(self, url:str):
        with open('List/common.txt', 'r') as file:
            contents = file.read()
            words = contents.split(url)
            
            for word in words:
                response = requests.get(f"{url}{word}")
                print(response)


    def scan(self):
        for path in self.common_paths:
            url = self.target_url + path
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Directory found: {url}")
                self.get_paths(url)
    

    def scan_founded_paths(self):
        for url in self.founded_paths:
            response = requests.get(url)
            print(response)