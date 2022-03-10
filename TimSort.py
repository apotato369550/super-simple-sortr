# work on timsort algorithm
from Algorithims import Algorithms
import time
import threading

class TimSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        n = len(data)
        minimum_run = self.minimum_run(n)

        for start in range(0, n, minimum_run):
            end = min(start + minimum_run - 1, n - 1)
            self.insertion_sort(data, start, end, drawData, delay)

        size = minimum_run
        while size < n:
            for left in range(0, n, 2 * size):
                middle = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))

                self.merge(data, left, middle, right, drawData, delay)

            size = 2 * size

        print(data)
        drawData(data, ["green" for x in range(len(data))])


    def minimum_run(self, length):
        r = 0
        while length >= 32:
            r |= length & 1
            length >>= 1
        return length + r

    def insertion_sort(self, data, left, right, drawData, delay):
        for i in range(left + 1, right + 1):
            for i in range(left + 1, right + 1):
                j = i
                while j > left and data[j] < data[j - 1]:
                    data[j], data[j - 1] = data[j - 1], data[j]
                    drawData(data, ["red" if x == j or x == j - 1 else "white" for x in range(len(data))])
                    time.sleep(delay)
                    j -= 1

    def merge(self, data, left, middle, right, drawData, delay):
        length_1, length_2 = middle - left + 1, right - middle
        left_partition, right_partition = [], []

        for i in range(0, length_1):
            left_partition.append(data[left + i])
        for i in range(0, length_2):
            right_partition.append(data[middle + 1 + i])

        i, j, k = 0, 0, left

        while i < length_1 and j < length_2:
            if left_partition[i] <= right_partition[j]:
                data[k] = left_partition[i]
                drawData(data, ["red" if x == k else "white" for x in range(len(data))])
                time.sleep(delay)
                i += 1
            else:
                data[k] = right_partition[j]
                drawData(data, ["red" if x == k else "white" for x in range(len(data))])
                time.sleep(delay)
                j += 1
            k += 1

        while i < length_1:
            data[k] = left_partition[i]

            k += 1
            i += 1

        while j < length_2:
            data[k] = right_partition[j]

            k += 1
            j += 1

