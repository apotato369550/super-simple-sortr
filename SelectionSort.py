from Algorithims import Algorithms
import time
import threading

class SelectionSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        # this works now yaasssssss
        for i in range(len(data)):
            minimum_index = i
            for j in range(i + 1, len(data)):
                drawData(data, ["yellow" if x == j or x == minimum_index else "white" for x in range(len(data))])
                time.sleep(delay)
                if data[minimum_index] > data[j]:
                    minimum_index = j

            drawData(data, [ "red" if x == i or x == minimum_index else "white" for x in range(len(data))])
            time.sleep(delay)

            data[i], data[minimum_index] = data[minimum_index], data[i]

            drawData(data, [ "red" if x == i or x == minimum_index else "white" for x in range(len(data))])
            time.sleep(delay)
        drawData(data, ["green" for x in range(len(data))])




