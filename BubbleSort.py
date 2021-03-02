from Algorithims import Algorithms
import time
import threading

class BubbleSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        # this doesn't work
        for _ in range(len(data) - 1):
            for i in range(len(data) - 1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    drawData(data, ["red" if x == i or x == i + 1 else "white" for x in range(len(data))])
                    time.sleep(delay)
        drawData(data, ["green" for x in range(len(data))])

