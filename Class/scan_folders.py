import os, stat


class ScanFolders:
    def __init__(self, path:str) -> None:
        self.path = path
        self.folder_list = []

    def scan(self) -> None:
       for dirpath, dirnames, filenames in os.walk(self.path):
          for filename in filenames:
               filepath = os.path.join(dirpath, filename)
               st = os.stat(filepath)
               self.folder_list.append({"path:": dirpath, "permission":stat.filemode(st.st_mode)})
               print(dirpath,stat.filemode(st.st_mode))