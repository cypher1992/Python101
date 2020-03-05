# Client
from com.project.src.PythonCrashCourse.ClassStructure.Stock import Stock

def main():
    bx = Stock("Blackstone", "BX", 25.67, "3-04-20")
    print(bx.toString())
    bx2 = bx.updatePriceWithDate(24.67, "3-05-20")
    print(bx2.toString())

main()
