class IOFile:

    def __init__(self):
        pass

    def readFile(path):
        listContent = []
        with open(path) as file_object:
            content = file_object.read()
            listContent.append(content)

        return listContent
