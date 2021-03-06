from Algorithims import Algorithms
import time
import threading

class QuickSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, 0, len(data) - 1, self.drawData, delay, True))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()



    def partition(self, data, head, tail, drawData, delay):
        border = head
        pivot = data[tail]

        drawData(data, self.getColorArray(len(data), head, tail, border, border))
        time.sleep(delay)

        for i in range(head, tail):
            if data[i] < pivot:
                drawData(data, self.getColorArray(len(data), head, tail, border, i, True))
                time.sleep(delay)

                data[border], data[i] = data[i], data[border]
                border += 1

            drawData(data, self.getColorArray(len(data), head, tail, border, i))
            time.sleep(delay)

        drawData(data, self.getColorArray(len(data), head, tail, border, tail, True))
        time.sleep(delay)
        data[border], data[tail] = data[tail], data[border]

        return border

    def sort(self, data, head, tail, drawData, delay, main):
        if head < tail:
            partition_index = self.partition(data, head, tail, drawData, delay)

            # Left partition
            self.sort(data, head, partition_index - 1, drawData, delay, False)

            # Right partition
            self.sort(data, partition_index + 1, tail, drawData, delay, False)

        if main:
            drawData(data, ["green" for x in range(len(data))])

    def getColorArray(self, data_length, head, tail, border, current_index, is_swapping=False):
        color_array = []

        for i in range(data_length):
            if i >= head and i <= tail:
                color_array.append("grey")
            else:
                color_array.append("white")

            if i == tail:
                color_array[i] = "blue"
            elif i == border:
                color_array[i] = "red"
            elif i == current_index:
                color_array[i] = "yellow"

            if is_swapping:
                if i == border or i == current_index:
                    color_array[i] = "green"

        return color_array