from . import Error


class DB:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "r+", encoding="UTF-8")
        self.Base = self.file.read().split("\n")[:-1]
        self.lists_id = []

        for line in self.Base:
            p = eval(line)
            self.lists_id.append(p["_id"])

    def create(self, name: dict):

        if name["_id"] in self.lists_id:
            return False

        self.file.write(str(name) + "\n")
        self.Base.append(str(name))
        self.lists_id.append(name["_id"])

    def search(self, _id):
        with open(self.file_name, encoding="UTF-8") as f:
            for line in f:
                try:
                    p = eval(line)
                    if p["_id"] == _id:
                        return p
                except:
                    return None

    def delete(self, _id):
        text = ""
        with open(self.file_name) as f:
            for line in f:
                try:
                    p = eval(line)
                    if p["_id"] != _id:
                        text += line
                except:
                    pass
        f = open(self.file_name, 'w')
        f.close()

        self.file.close()
        self.file = open(self.file_name, "r+")
        self.Base = self.file.read()
        self.file.write(text)

    def amount_documents(self):
        lines = 0
        for _ in open(self.file_name):
            lines += 1
        return lines

    def update(self, dicts: dict):
        text = ""
        with open(self.file_name) as f:
            for line in f:
                try:
                    p = eval(line)
                    if p["_id"] != dicts["_id"]:
                        text += line
                except:
                    pass
        f = open(self.file_name, 'w')
        f.close()

        self.file.close()
        self.file = open(self.file_name, "r+")
        self.Base = self.file.read()
        self.file.write(text)
        self.file.write(str(dicts)+"\n")

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return True
