from Algorithims import Algorithms
import time
import threading


class MergeSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        self.algorithm(data, 0, len(data) - 1, drawData, delay)
        drawData(data, ["green" for x in range(len(data))])
        print data

    def algorithm(self, data, left, right, drawData, delay):
        if left < right:
            middle = (left + right) // 2
            self.algorithm(data, left, middle, drawData, delay)
            self.algorithm(data, middle + 1, right, drawData, delay)
            self.merge(data, left, middle, right, drawData, delay)

    def merge(self, data, left, middle, right, drawData, delay):
        drawData(data, self.getColorArray(len(data), left, middle, right))
        time.sleep(delay)

        # left partition
        left_partition = data[left: middle + 1]

        # right partition
        right_partition = data[middle + 1: right + 1]

        left_index = 0
        right_index = 0

        for data_index in range(left, right + 1):
            if left_index < len(left_partition) and right_index < len(right_partition):
                if left_partition[left_index] <= right_partition[right_index]:
                    data[data_index] = left_partition[left_index]
                    left_index += 1
                else:
                    data[data_index] = right_partition[right_index]
                    right_index += 1
            elif left_index < len(left_partition):
                data[data_index] = left_partition[left_index]
                left_index += 1
            else:
                data[data_index] = right_partition[right_index]
                left_index += 1

            drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
            time.sleep(delay)

    def getColorArray(self, length, left, middle, right):
        color_array = []

        for i in range(length):
            if i >= left and i <= right:
                if i >= left and i <= middle:
                    color_array.append("yellow")
                else:
                    color_array.append("red")
            else:
                color_array.append("white")

        return color_array
        # Test this tonight