# Multicore threading
# Model for Multicore threading: https://medium.com/@urban_institute/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba
import time
import multiprocessing

# Setup

def sleepByFunc():
    time.sleep(1)

def createList():
    sleepByFunc()
    return []

def getData(lst,multiplier=1):
    for i in range(0,10):
        lst.append(i*multiplier)
        sleepByFunc()

    return lst

def filterList(lst,mod=2):
    newLst = []
    for i in lst:
        if(i%mod == 0):
            newLst.append(i)
            sleepByFunc()

    return newLst


if(__name__ == "__main__"):
    starttime = time.time()
    manager = multiprocessing.Manager()
    return_list = manager.list()
    process =multiprocessing.Process(target=createList)
    process.start()
    process.join()
    # emptylist = createList()
    print(return_list)
    lst = getData(return_list)
    print(lst)
    filter = filterList(lst)
    print(filter)
    print(time.time() - starttime)

#main()