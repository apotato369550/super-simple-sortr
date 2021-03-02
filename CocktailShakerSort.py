from Algorithims import Algorithms
import time
import threading

# continue shit here
class CocktailShakerSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        # this did not work. figure out what went wrong
        length = len(data)
        swapped = True
        start = 0
        end = length - 1
        while swapped:
            swapped = False

            for i in range(start, end):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    drawData(data, ["red" if x == i or x == i + 1 else "white" for x in range(len(data))])
                    time.sleep(delay)
                    swapped = True
            if not swapped:
                break

            swapped = False

            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    drawData(data, ["red" if x == i or x == i + 1 else "white" for x in range(len(data))])
                    time.sleep(delay)
                    swapped = True

            start = start + 1

        drawData(data, ["green" for x in range(len(data))])

