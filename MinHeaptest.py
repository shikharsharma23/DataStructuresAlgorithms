from MinHeap import *

array = [3,7,2,10,5,11,4,13,10]
min_heap = MinHeap(80)
array_min_heap = min_heap.buildMinHeap(array)
min_heap.print()
print('\n')
min_heap.insert(1)
min_heap.print()
min_heap.remove()
print('\n')
min_heap.print()