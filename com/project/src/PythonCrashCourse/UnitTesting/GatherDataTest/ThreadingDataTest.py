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
