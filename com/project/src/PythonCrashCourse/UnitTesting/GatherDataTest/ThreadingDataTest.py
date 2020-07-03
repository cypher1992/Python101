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
        t1 = threading.Thread(target=que.put(gd.getDataSource1))
        t2 = threading.Thread(target=que.put(gd.getDataSource2))
        t3 = threading.Thread(target=que.put(gd.getDataSource3))
        t4 = threading.Thread(target=que.put(gd.getDataSource4))
        threadList = [t1,t2,t3,t4]
        for thread in threadList:
            thread.start()
        for thread in threadList:
            thread.join()
        finish = time.perf_counter()
        print(finish-start)
        #print(que.get()()) need to use extra pair of parenthesis to return value
        self.assertTrue(finish - start < 2)

    def test_threadQueStoreListreturnsFirstIndex(self):
        que = queue.Queue()
        gd = GatherData()
        t1 = threading.Thread(target=que.put(gd.getDataSource1))
        t2 = threading.Thread(target=que.put(gd.getDataSource2))
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
        t1 = threading.Thread(target=que.put(gd.getDataSource1))
        t2 = threading.Thread(target=que.put(gd.getDataSource2))
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

    def test_threadQueStoreListreturnsThirdIndex(self):
        que = queue.Queue()
        gd = GatherData()
        t1 = threading.Thread(target=que.put(gd.getDataSource1))
        t2 = threading.Thread(target=que.put(gd.getDataSource2))
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

    def test_threadQueStoreListreturnsFourthIndex(self):
        que = queue.Queue()
        gd = GatherData()
        t1 = threading.Thread(target=que.put(gd.getDataSource1))
        t2 = threading.Thread(target=que.put(gd.getDataSource2))
        t3 = threading.Thread(target=que.put(gd.getDataSource3))
        t4 = threading.Thread(target=que.put(gd.getDataSource4))
        threadList = [t1,t2,t3,t4]
        for thread in threadList:
            thread.start()
        for thread in threadList:
            thread.join()
        que.get()()
        que.get()()
        que.get()()
        actual = que.get()()
        expected = []
        for i in range(8):
            if (i % 4 == 0):
                expected.append(i)
        self.assertEqual(expected,actual)

    def test_threadDataDurationOfThreadsIsLessThan2Sec(self):
        que = queue.Queue()
        gd = GatherData()
        td = ThreadingData()
        start = time.perf_counter()
        t1 = td.createThread(function=que.put(gd.getDataSource1))
        t2 = td.createThread(function=que.put(gd.getDataSource2))
        td.startThread(t1)
        td.startThread(t2)
        td.joinThread(t1)
        td.joinThread(t2)
        finish = time.perf_counter()
        print(finish-start)
        print(que.get()())
        self.assertTrue(finish-start < 2)

    def test_threadDataQueGetThread2DurationOfThreadsIsLessThan2Sec(self):
        que = queue.Queue()
        gd = GatherData()
        td = ThreadingData()
        start = time.perf_counter()
        t1 = td.createThread(function=que.put(gd.getDataSource1))
        t2 = td.createThread(function=que.put(gd.getDataSource2))
        td.startThread(t1)
        td.startThread(t2)
        td.joinThread(t1)
        td.joinThread(t2)
        finish = time.perf_counter()
        que.get()()
        print(que.get()())
        self.assertTrue(finish-start < 2)

    def test_threadDataDictionaryDurationOfThreadsIsLessThan2Sec(self):
        dictThread = {}
        gd = GatherData()
        td = ThreadingData()
        start = time.perf_counter()
        t1 = td.createThread(function=dictThread.update({"thread1":gd.getDataSource1}))
        t2 = td.createThread(function=dictThread.update({"thread2":gd.getDataSource2}))
        td.startThread(t1)
        td.startThread(t2)
        td.joinThread(t1)
        td.joinThread(t2)
        finish = time.perf_counter()
        print(dictThread.get("thread1")())
        self.assertTrue(finish-start < 2)

    def test_threadDataDictionaryGetThread2DurationOfThreadsIsLessThan2Sec(self):
        dictThread = {}
        gd = GatherData()
        td = ThreadingData()
        start = time.perf_counter()
        t1 = td.createThread(function=dictThread.update({"thread1":gd.getDataSource1}))
        t2 = td.createThread(function=dictThread.update({"thread2":gd.getDataSource2}))
        td.startThread(t1)
        td.startThread(t2)
        td.joinThread(t1)
        td.joinThread(t2)
        finish = time.perf_counter()
        print(dictThread.get("thread2")())
        self.assertTrue(finish-start < 2)


    def test_threadDataDictionaryGetThread4DurationIsLessThan2Sec(self):
        dictThread = {}
        gd = GatherData()
        td = ThreadingData()
        start = time.perf_counter()
        t1 = td.createThread(function=dictThread.update({"thread1":gd.getDataSource1}))
        t2 = td.createThread(function=dictThread.update({"thread2":gd.getDataSource2}))
        t3 = td.createThread(function=dictThread.update({"thread3": gd.getDataSource3}))
        t4 = td.createThread(function=dictThread.update({"thread4": gd.getDataSource4}))
        threadList = [t1,t2,t3,t4]

        for thread in threadList:
            td.startThread(thread)

        for thread in threadList:
            td.joinThread(thread)

        finish = time.perf_counter()
        print(dictThread.get("thread4")())
        self.assertTrue(finish-start < 2)

    def test_MainThreadDictionaryGetThread4DurationIsMoreThan5Sec(self):
        dictThread = {}
        gd = GatherData()
        dictThread.update({})
        start = time.perf_counter()
        dictThread.update({"datasrc1": gd.getDataSource1})
        dictThread.update({"datasrc2": gd.getDataSource2})
        dictThread.update({"datasrc3": gd.getDataSource3})
        dictThread.update({"datasrc4": gd.getDataSource4})

        for i in range(1,5):
            string = "datasrc" + str(i)
            print(dictThread.get(string)())

        finish = time.perf_counter()
        self.assertTrue(finish - start > 4)

    def test_ThreadDictionaryGetThreads15DurationIsMoreThan3Sec(self):
        dictThread = {}
        gd = GatherData()
        td = ThreadingData()
        start = time.perf_counter()
        t1 = td.createThread(function=dictThread.update({"thread1": gd.getDataSource1}))
        t2 = td.createThread(function=dictThread.update({"thread2": gd.getDataSource5}),arguments=[2])
        threadList = [t1,t2]
        for thread in threadList:
            td.startThread(thread)
        for thread in threadList:
            td.joinThread(thread)

        finish = time.perf_counter()

        self.assertTrue(finish-start<3)

