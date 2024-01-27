import time as T

# seconds = T.time()
# print ("Seconds since epoch =", seconds)

# local_time = T.ctime(seconds)
# print("Local time:", local_time)

# print("Printed immediately")
# T.sleep(5)
# print("Printed after 5 seconds")

i=0
for c in "HELLO":
    print(i*" "+c)
    i+=1
    T.sleep(.5)
