from Algorithims import Algorithms
import time
import threading

class ShellSort(Algorithms):
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
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i

                while j >= gap and data[j - gap] > temp:

                    data[j] = data[j - gap]

                    drawData(data, ["red" if x == j or x == j - gap else "white" for x in range(len(data))])
                    time.sleep(delay)

                    j -= gap

                data[j] = temp

                drawData(data, ["red" if x == j or x == i - gap else "white" for x in range(len(data))])
                time.sleep(delay)

            gap //= 2
        drawData(data, ["green" for x in range(len(data))])
