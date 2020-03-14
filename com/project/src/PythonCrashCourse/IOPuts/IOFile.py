class IOFile:

    def __init__(self):
        pass

    def readFileByLine(path):
        listContent = []
        with open(path) as file_object:
            for line in file_object:
                listContent.append(line.strip())

        return listContent
