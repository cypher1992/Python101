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

    def test_durationOfThreadsIsLessThan3Sec(self):
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

    def test_implementDurationOfThreadsIsLessThan2Sec(self):
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

    def test_durationOfMainThreadIsAtleast4Sec(self):
        start = time.perf_counter()
        gd = GatherData()
        gd.getDataSource1()
        gd.getDataSource2()
        gd.getDataSource3()
        gd.getDataSource4()
        finish = time.perf_counter()
        print(finish-start)
        self.assertTrue(finish-start>4)

    def test_implementDurationOfThreadsIsLessThan2Sec(self):
        que = queue.Queue()
        start = time.perf_counter()
        gd = GatherData()
        t1 = threading.Thread(target = que.put(gd.getDataSource1))
        t2 = threading.Thread(target = que.put(gd.getDataSource2))
        t3 = threading.Thread(target=que.put(gd.getDataSource3))
        t4 = threading.Thread(target=que.put(gd.getDataSource4))
        threadList = [t1,t2,t3,t4]
        for thread in threadList:
            thread.start()
        for thread in threadList:
            thread.join()
        finish = time.perf_counter()
        #print(que.get()()) need to use extra pair of parenthesis to return value
        self.assertTrue(finish - start < 2)

    def test_threadQueStoreListreturnsFirstIndex(self):
        que = queue.Queue()
        gd = GatherData()
        t1 = threading.Thread(target = que.put(gd.getDataSource1))
        t2 = threading.Thread(target = que.put(gd.getDataSource2))
        t3 = threading.Thread(target=que.put(gd.getDataSource3))
        t4 = threading.Thread(target=que.put(gd.getDataSource4))
        threadList = [t1,t2,t3,t4]
        for thread in threadList:
            thread.start()
        for thread in threadList:
            thread.join()
        actual = que.get()()
        expected = []
        for i in range(1000000):
            expected.append(i)
        self.assertEqual(expected,actual)

    def test_threadQueStoreListreturnsSecondIndex(self):
        que = queue.Queue()
        gd = GatherData()
        t1 = threading.Thread(target = que.put(gd.getDataSource1))
        t2 = threading.Thread(target = que.put(gd.getDataSource2))
        t3 = threading.Thread(target=que.put(gd.getDataSource3))
        t4 = threading.Thread(target=que.put(gd.getDataSource4))
        threadList = [t1,t2,t3,t4]
        for thread in threadList:
            thread.start()
        for thread in threadList:
            thread.join()
        que.get()()
        actual = que.get()()
        expected = []
        for i in range(100, 1000, 2):
            expected.append(i)
        self.assertEqual(expected,actual)

    def test_threadQueStoreListreturnsThirdIndex(self):
        que = queue.Queue()
        gd = GatherData()
        t1 = threading.Thread(target = que.put(gd.getDataSource1))
        t2 = threading.Thread(target = que.put(gd.getDataSource2))
        t3 = threading.Thread(target=que.put(gd.getDataSource3))
        t4 = threading.Thread(target=que.put(gd.getDataSource4))
        threadList = [t1,t2,t3,t4]
        for thread in threadList:
            thread.start()
        for thread in threadList:
            thread.join()
        que.get()()
        que.get()()
        actual = que.get()()
        expected = []
        for i in range(10000000, 20000000, 2500):
            expected.append(i)
        self.assertEqual(expected,actual)

