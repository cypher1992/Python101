class IOFile:

    def __init__(self):
        pass

    def readFileByLine(path):
        listContent = []
        with open(path) as file_object:
            for line in file_object:
                listContent.append(line.strip())

        return listContent

    def readDelimterByLine(self,path,delimiter):
        listLine = self.readFileByLine(path)
        map = {}
        for line in listLine:
            locationDelimiter = line.find(delimiter)
            key,value = line[:locationDelimiter] , line[locationDelimiter+1:]
            map[key] = value
        print(map)

        return map

    def writeToFileDelimiter(self,path,value,key,delimiter):
        with open(path,'w') as file_object:
            file_object.write(value + delimiter + key)


    # Next test
    def appendToFileDelimiter(self,path,value,key,delimiter):
        with open(path,'a') as file_object:
            file_object.write(value + delimiter + key +'\n')
            file_object.close()