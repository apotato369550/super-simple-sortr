from Algorithims import Algorithms
import time
import threading

class CountSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        max_value = 0

        for value in data:
            if value > max_value:
                max_value = value

        max_value = max_value + 1
        count = [0] * max_value

        for value in data:
            count[value] += 1

            drawData(data, ["yellow" if x == value else "white" for x in range(len(data))])
            time.sleep(delay)

        i = 0

        for a in range(max_value):
            for j in range(count[a]):
                data[i] = a
                i += 1

                drawData(data, ["red" if x == i else "white" for x in range(len(data))])
                time.sleep(delay)


