"""
  +----------------+
  |################|
  |#Break##########|
  |#####And########|
  |#######Continue#|
  |####Lil#Pass####|
  +----------------+

  Break - gets out of the loop
  Continue - Stays within the Loop
  Pass - does nothing, but when statement requires a return
"""

for i in range(0,10,1):
    if( i == 4):
        print(i)
        continue
    elif(i == 8):
        print(i)
        break
    else:
        pass