def parent(i):
    return i//2
def left(i):
    return 2*i
def right(i):
    return (2*i)+1

def heapExtractMin(a):
    size = len(a) - 1
    if size < 1:
        return ()
    minValue = a[1]
    a[1] = a[size]
    size -=1
    minHeapify(a,1,size)
    return minValue, a[:-1]

def minHeapify(a:list, i:int, hLen:int):
    l =  left(i)
    r = right(i)
    if l <= hLen and a[l][0]<a[i][0]:
        minValue = l
    else:
        minValue = i
    if r <= hLen and a[r][0]<a[minValue][0]:
        minValue = r
    if minValue != i:
        aux = a[minValue]
        a[minValue] = a[i]
        a[i] = aux
        minHeapify(a,minValue,hLen)

def buildMinHeap(a:list):
    size = len(a) - 1
    for i in range((size//2), 0,-1):
        minHeapify(a,i,size)
    return a