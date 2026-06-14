def mergesort(arr):
	# print("calling mergesort: %s" % (arr))
	if len(arr) < 2:
		return
	# Find middle point to divide subarray in half
	middle = len(arr) // 2 # // is Python operator for integer division
	left = arr[:middle]
	right = arr[middle:]
	# Call mergesort for left
	mergesort(left)
	# Call mergesort for right
	mergesort(right)
	# Merge the two (now sorted) halves
	merge(arr, left, right)

def merge(arr, left, right):
	# Merge the two subarrays
	# Merge the arrays back into arr
	# print ("merging %s %s" % (left, right))
	i = 0		# Start at 0 for left array
	j = 0		# Start at 0 for right array
	k = 0 		# Start at 0 in array to-be-merged
	while i < len(left) and j < len(right):
		# Find the smaller value between the two arrays to be merged
		# And insert it into the final array at position k
		if left[i] < right[j]:
			# Left has the smaller value, and should be inserted first
			arr[k] = left[i]
			i += 1
		else:
			# Right has the smaller value, and should be inserted first
			arr[k] = right[j]
			j += 1
		k += 1
	# If there are any leftover elements in left, copy them
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	# If there are any leftover elements in right, copy them
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
	# print("merged: %s" % arr)
def quicksort(arr):
	_quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, low, high):
	if low < high: 						# if low == high, we are done (1 element in array, so it's as sorted as it gets)
		p = partition(arr, low, high) 	# Put one element in right place; move other elements left or right of it based on size
# NOTE: The following line is the only difference between Lomuto and Hoare.
# Notice the left half quicksort is from low to p-1 in Lomuto.
		_quicksort(arr, low, p - 1) 	# Sort left half, before the sorted element
		_quicksort(arr, p + 1, high)	# Sort right half, after the sorted element

def partition(arr, low, high):			# We already know low < high, so there's at least 2 elements in arr
	# Optional: Set pivot as median of three values, and swap to last position
	pivot = arr[high]					# Set pivot to highest value. We will deal with everything before it, iterating
	wall = low							# Everything left of wall has been checked and is less than pivot
	i = low								# Counter for each element
	while i < high:						# For each element, EXCLUDING the pivot, we will check if less than pivot.
		if arr[i] < pivot:				# We found something to put behind the wall!
			swap(arr, wall, i)			# Swap element at i to be behind the wall.
			wall += 1					# Move the wall up by one.
		i += 1
	swap(arr, wall, high)					# Swap the high index (the pivot index) into it's new place. All to left of it is less, all to right greater than or equal
	return wall

def swap(arr, i, j):					# Swap indices i and j in arr
	tmp = arr[i]						# Set i's value to tmp, to prevent overwriting it
	arr[i] = arr[j]						# Swap j's value into i's place
	arr[j] = tmp						# Swap i's value into j's place
def quicksort(arr):
	_quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, low, high):
	if low < high: 						# if low == high, we are done (1 element in array, so it's as sorted as it gets)
		p = partition(arr, low, high) 	# Put one element in right place; move other elements left or right of it based on size
# NOTE: The following line is the only difference between Lomuto and Hoare.
# Notice the left half quicksort is from low to p in Hoare.
		_quicksort(arr, low, p) 	# Sort left half, before the sorted element
		_quicksort(arr, p + 1, high)	# Sort irght half, after the sorted element

def partition(arr, low, high):			# We already know low < high, so there's at least 2 elements in arr
	# Optional: Set pivot as median of three values, and swap to last position
	pivot = arr[low] 					# Pivot is lower part.
	i = low - 1								# Set left hand index to the first element
	j = high + 1							# Set right hand index to the last element.
	while True:
#		print('we out here piv%s lo%s hi%s' % (pivot, low, high))
#		print('arr[i] = %s; arr[j] = %s' % (arr[i],arr[j]))
		while True:			# If less than pivot AND on left (i) side, it's okay. No action needed.
			i += 1						# Slide past this element and check the next one, moving toward the middle
			if not (i < j and arr[i] < pivot): break
		while True:			# If greater than pivot AND on right (j) side, it's okay. No action needed.
			j -= 1						# Slide past this element and check the next one, moving toward the middle
			if not (i < j and arr[j] > pivot): break
		if i >= j:						# i >= j indicates that the two indexes have converged in the middle; we are done swapping
			return j					# j is the location where the pivot should be
		swap(arr, i, j)					# Otherwise, i and j point to two elements in the wrong half of the array. Swap them and both will be corrected.

def swap(arr, i, j):					# Swap indices i and j in arr
	tmp = arr[i]						# Set i's value to tmp, to prevent overwriting it
	arr[i] = arr[j]						# Swap j's value into i's place
	arr[j] = tmp						# Swap i's value into j's place
def bubblesort(arr):
	while True:
		haveSwitched = False
		# One pass of swaps
		for i in range(1, len(arr)):
			if arr[i - 1] > arr[i]:
				haveSwitched = True 
				tmp = arr[i - 1]
				arr[i - 1] = arr[i]
				arr[i] = tmp
		if not haveSwitched:
			break
def insertionsort(arr):
	for i in range(1,len(arr)): # Start at element 1. Everything before is already sorted. 
		j = i # Start at j and work our way backward to find the spot in sorted array
		while j > 0 and arr[j-1] > arr[j]: # If the previous element is greater, swap our way backward
			temp = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] = temp
			j -= 1
import unittest
import mergesort, quicksort_lomuto, quicksort_hoare, bubblesort, insertionsort

class TestSorts(unittest.TestCase):
	def setUp(self):
		self.arrs = [
			[9,8,7,6,5,4,3,2,1],
			[1,2,3,4],
			[5,5,5,4],
		]
		self.arrs_sorted = [
			[1,2,3,4,5,6,7,8,9],
			[1,2,3,4],
			[4,5,5,5],
		]
	# Generic helper method for testing each sort
	def _test_sort(self, func):
		for i,arr in enumerate(self.arrs):
			# Sort test array
			func(arr)
			# Make sure it was sorted correctly
			self.assertEqual(self.arrs_sorted[i], arr)	
	def test_mergesort(self):
		self._test_sort(mergesort.mergesort)
	def test_hoare(self):
		self._test_sort(quicksort_hoare.quicksort)
	def test_lomuto(self):
		self._test_sort(quicksort_lomuto.quicksort)
	def test_bubblesort(self):
		self._test_sort(bubblesort.bubblesort)
	def test_insertionsort(self):
		self._test_sort(insertionsort.insertionsort)

if __name__ == '__main__':
    unittest.main(verbosity=2)
