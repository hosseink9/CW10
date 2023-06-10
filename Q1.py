# In the name of GOD


class FileReader:
    def __init__(self, filename: str, mode='rt'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb,1000)
        self.file.close()


with FileReader("../my_test.txt", "a+") as f:
    f.write("hellooooo")
