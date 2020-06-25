import unittest, time, threading, queue
from com.project.src.Experimentation.GatherDataWithThreads.GatherData import GatherData
from com.project.src.Experimentation.GatherDataWithThreads.ThreadingData.ThreadData import ThreadingData

class ThreadingDataTest(unittest.TestCase):


    def test_durationOfThreadIsAtleast3Sec(self):
        start = time.perf_counter()
        gd = GatherData()
        gd.getDataSource1()
        gd.getDataSource3()
        finish = time.perf_counter()
        self.assertTrue(finish-start>3)

    def test_duractionOfThreadsIsLessThan3Sec(self):
        start = time.perf_counter()
        gd = GatherData()
        td = ThreadingData()
        # when it comes to using the function in thread. No Parenthesis
        thread = td.createThread(function=gd.getDataSource1)
        thread2 = td.createThread(function=gd.getDataSource3)
        td.startThread(thread)
        td.startThread(thread2)
        threadList = []
        threadList.append(thread)
        threadList.append(thread2)
        td.joinThread(thread)
        td.joinThread(thread2)
        finish = time.perf_counter()
        self.assertTrue(finish-start < 3)

    def test_implementDuractionOfThreadsIsLessThan2Sec(self):
        que = queue.Queue()
        start = time.perf_counter()
        gd = GatherData()
        t1 = threading.Thread(target = que.put(gd.getDataSource1))
        t2 = threading.Thread(target = que.put(gd.getDataSource1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        finish = time.perf_counter()
        print(que.qsize())
        self.assertTrue(finish - start < 2)


