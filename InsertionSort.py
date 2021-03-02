from Algorithims import Algorithms
import time
import threading

class InsertionSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        # the yellow line works correctly, but somehow the swap doesn't?
        for i in range (1, len(data)):
            key = data[i]

            j = i - 1
            drawData(data, ["red" if x == j + 1 else "white" for x in range(len(data))])
            time.sleep(delay)
            while j >= 0 and key < data[j]:
                drawData(data, ["yellow" if x == j else "white" for x in range(len(data))])
                time.sleep(delay)
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = key
            drawData(data, ["red" if x == j + 1 else "white" for x in range(len(data))])
            time.sleep(delay)
        self.drawData(data, ["green" for x in range(len(data))])
        # implement sorting pattern


