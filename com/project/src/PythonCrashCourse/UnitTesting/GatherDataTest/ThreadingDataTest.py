import unittest
import time
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
        thread = td.createThread(function=gd.getDataSource1())
        thread2 = td.createThread(function=gd.getDataSource3())
        td.startThread(thread)
        td.startThread(thread2)
        threadList = []
        threadList.append(thread)
        threadList.append(thread2)
        td.joinThread(thread)
        td.joinThread(thread2)
        finish = time.perf_counter()
        self.assertTrue(finish-start < 3)
