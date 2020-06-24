import threading
class ThreadingData():

    def createThread(self,function=None):
        return threading.Thread(target=function)

    def startThread(self, thread=None):
        thread.start()

    def joinThread(self,thread=None):
        thread.join()
