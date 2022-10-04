import time
st = time.time()

###########################

li = [5,4,8,15,14,17,49,58,12,18,16,13,25,11]
num = 16
li.sort()

print(li)

def biSer(li, num):
    l = 0
    r = len(li)-1
    while l <= r:
        m = int((l+r)/2)
        if num == li[m]:
            return m
        elif num < li[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

print(biSer(li,num))



####################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
