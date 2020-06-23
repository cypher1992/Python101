import threading
class ThreadingData():

    def createThread(self,function=None):
        return threading.Thread(target=function)
         