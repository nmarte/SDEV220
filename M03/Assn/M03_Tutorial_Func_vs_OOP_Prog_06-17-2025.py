Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     # Function to sort an array of 0s, 1s, and 2s
...     def sort012(self, arr):
...         # code here
...         low, mid, high = 0,0, len(arr) - 1
...         
...         while mid <= high:
...             if arr[mid] == 0:
...                 arr[low], arr[mid] = arr[mid], arr[low]
...                 low += 1
...                 mid += 1
...             elif arr[mid] == 1:
...                 mid += 1
...             else:
...                 arr[mid], arr[high] = arr[high], arr[mid]
