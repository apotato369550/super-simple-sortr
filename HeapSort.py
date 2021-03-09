from Algorithims import Algorithms
import time
import threading


class HeapSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        self.algorithm(data, drawData, delay)
        print(data)

        drawData(data, ["green" for x in range(len(data))])
        time.sleep(delay)

    def algorithm(self, data, drawData, delay):
        n = len(data)

        for i in range(n // 2 - 1, -1, -1,):
            self.heapify(data, n, i, drawData, delay)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.heapify(data, i, 0, drawData, delay)

    def heapify(self, data, n, i, drawData, delay):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[largest] < data[left]:
            largest = left

        if right < n and data[largest] < data[right]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]

            drawData(data, self.getColorArray(len(data), n))
            time.sleep(delay)

            self.heapify(data, n, largest, drawData, delay)

    def getColorArray(self, length, n):
        color_array = []

        for x in range(length):
            if x == n:
                color_array.append("red")
            elif x > n:
                color_array.append("white")
            else:
                color_array.append("yellow")


        return color_array