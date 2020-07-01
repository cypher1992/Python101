import threading
class ThreadingData():

    def createThread(self,function=None, arguments = None):
        return threading.Thread(target=function, args = arguments)

    def startThread(self, thread=None):
        thread.start()

    def joinThread(self,thread=None):
        thread.join()
