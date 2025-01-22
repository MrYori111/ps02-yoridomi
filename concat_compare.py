import time

start = time.time()
result = "".join (str(i)
for i in range(1,100001))
result += str(id)
print("join() Time:", time.time () - start)
