import time

# seconds = time.time()
# print ("Seconds since epoch =", seconds)

# local_time = time.ctime(seconds)
# print("Local time:", local_time)

# print("Printed immediately")
# time.sleep(5)
# print("Printed after 5 seconds")

i=0
for c in ("HELLO"):
    print(i*" "+c)
    i+=1
    time.sleep(.5)
