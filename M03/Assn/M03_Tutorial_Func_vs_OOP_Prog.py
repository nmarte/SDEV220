class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n = len(arr) # keeps track of the length of the array / or num of elements
        lo = 0      # low point / initialized @ zero
        hi = n-1    # high point / initialized @ last element
        mid = 0     # mid point / initialized @ zero
        # Iterate until all the elements are sorted
        while mid <= hi:        # While the midddle value is less than or equal to the highest value
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]   # If mid value is zero then a swap is performed
                lo += 1         # Afer the swap, the low and middle values (swapped values)
                mid += 1        # are increased by one
            elif arr[mid] == 1:
                mid += 1
            else:               # if mid value is neither zero nor 1, then;
                arr[mid], arr[hi] = arr[hi], arr[mid]   # a swap is performed between mid and high values.
                hi -= 1
        return arr


def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()