import json


class JsonHadler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.data = None

    def file_load(self):
        self.file = open(self.filename, "r")
        self.data = json.load(self.file)
        self.file.close()
        self.file = open(self.filename, "w")

    def file_save(self):
        json.dump(self.data, self.file, ensure_ascii=False)

    def file_expense_add(self, expense):
        self.data["expenses"].append(expense)

    def file_close(self):
        self.file.close()
