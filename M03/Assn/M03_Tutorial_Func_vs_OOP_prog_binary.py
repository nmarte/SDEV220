class Solution:

    def binarysearch(self, arr, k):
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == k:
                result = mid
                right = mid - 1  # Search in the left half for the first occurrence
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        return result

class Solution:
    def binarysearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (low + high) // 2
            if arr[mid] == k:
                return mid
                high = mid - 1
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return -1