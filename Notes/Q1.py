import heapq

# Creating a Heap Queue
# 1. heapq.heapify(x); Parameter: x list to be converted into a heap.

nums = [10, 20, 15, 30, 40]
heapq.heapify(nums)
print("Heap queue:", nums)


# 2. Convert into a max-heap by inverting values  
max_heap = [-n for n in nums]

#The above is the same as the below
# max_heap = []
# for n in nums:
#     max_heap.append(-n)

heapq.heapify(max_heap)
print(max_heap)
# Access largest element (invert sign again)  
print("Largest element:", -max_heap[0])


# 3. Appending and Popping Elements
# heapq.heappush(heap, item) : adds a new element to the heap.
# heapq.heappop(heap) : removes and returns the smallest element.

heapq.heappush(nums, 15)
min = heapq.heappop(nums)

print("Smallest : ", min)
print(nums)

heapq.heappush(nums, 25)
min = heapq.heappop(nums)
print("Smallest : ", min)
print(nums)


# 4. Appending and Popping Simultaneously
# Push a new element (18) and pop the smallest element at the same time
min = heapq.heappushpop(nums, 18)
print("Smallest : ", min)
print(nums)


# 5. Finding Largest and Smallest Elements
# heapq.nlargest(n, iterable) : returns the n largest elements from the iterable.
# heapq.nsmallest(n, iterable) : returns the n smallest elements from the iterable.

maxi = heapq.nlargest(3, nums)
print("3 largest elements:", maxi)

min = heapq.nsmallest(2, nums)
print("2 smallest elements:", min)

# 6. Replace and Merge Operations

# heapq.heapreplace() function is a combination of pop and push
# It returns the smallest element before replacing it.
min = heapq.heapreplace(nums, 21)
print("Smallest :", min)
print(nums)


# heapq.merge() merge multiple sorted iterables into a single sorted heap. 
# It returns an iterator over the sorted values, which we can then iterate through.
h2 = [19, 22, 23, 24]
h3 = list(heapq.merge(nums, h2))
print("Merged Heap:", h3)