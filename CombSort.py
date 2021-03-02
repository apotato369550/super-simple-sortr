from Algorithims import Algorithms
import time
import threading

class CombSort(Algorithms):
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
        gap = n
        swapped = True

        while gap != 1 or swapped == 1:
            gap = self.nextGap(gap)
            swapped = False
            for i in range(0, n - gap):
                if data[i] > data[i + gap]:
                    data[i], data[i + gap] = data[i + gap], data[i]

                    drawData(data, ["red" if x == i or x == i + gap else "white" for x in range(len(data))])
                    time.sleep(delay)

                    swapped = True
        # this works properly as it should
        drawData(data, ["green" for x in range(len(data))])
        time.sleep(delay)

    def nextGap(self, gap):
        gap = (gap * 10)/13
        if gap < 1:
            return 1
        return gap

    # test this out later

