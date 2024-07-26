class Solution(object):
    def sortPeople(self, names, heights):
        arr = list(zip(names, heights))
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j][1] < arr[j+1][1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        sorted_names = [name for name, height in arr]
        return sorted_names