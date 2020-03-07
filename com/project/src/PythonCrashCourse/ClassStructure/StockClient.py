# Client
from com.project.src.PythonCrashCourse.ClassStructure.Stock import Stock

def main():
    bx = Stock("Blackstone", "BX", 25.67, "3-04-20")
    print(bx.toString())
    bx2 = bx.updatePriceWithDate(24.67, "3-05-20")
    # both bx and bx2 are pointed to the same instance causeing to reflect new values from change
    print(bx.toString())
    print(bx2.toString())

    #instance variables can be updated without getters and setters
    #blackstone ticket was updated by the sec
    bx.ticker = "BXX"
    print(bx.toString())
    bx.setCompany("BlackStone")
    bx.setDate("3-6-20")
    bx.setPrice(29.64)
    bx.setTicker("BX")
    print(bx.getCompany(),bx.getDate(),bx.getTicker(),bx.getPrice(),bx.getID())

main()
