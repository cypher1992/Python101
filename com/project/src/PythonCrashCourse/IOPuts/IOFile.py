class IOFile:

    def __init__(self):
        pass

    def readFileByLine(path):
        listContent = []
        with open(path) as file_object:
            for line in file_object:
                listContent.append(line.strip())
        file_object.close()

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

    def writeToFileDelimiter(self,path,key,value,delimiter):
        with open(path,'w') as file_object:
            file_object.write( key + delimiter + value)
        file_object.close()

    def appendToFileDelimiter(self,path,key,value,delimiter):
        with open(path,'a') as file_object:
            file_object.write(key + delimiter + value +'\n')
        file_object.close()
    #TESTING IN PROGRESS
    def updateToFileDelimiter(self,path,key, value,delimiter):
        map = self.readDelimterByLine(path,delimiter)
        map.update(key, value)
        for k,v in map.items():
            self.appendToFileDelimiter(path,k,v,delimiter)

    def deleteContentFile(self,path):
        str=''
        with open(path,'w') as file_object:
            file_object.write(str)
        file_object.close()