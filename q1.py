
class FileReader:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
            # print(exc_type, "1111")
            # print(exc_value, "2222")
            # print(exc_traceback, "3333")
            self.file.close()


with FileReader('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)

