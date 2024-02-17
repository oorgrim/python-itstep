from functools import lru_cache

with open("Feb-16/example.txt", "w") as file:
    file.write("Hello world!")

class FileReader:
    def __init__(self, path):
        self.path = path

    @lru_cache
    def read_file(self):
        with open(self.path, 'r') as file:
            content = file.read()
        return content

file_reader = FileReader("Feb-16/example.txt")

content1 = file_reader.read_file()
print(content1)