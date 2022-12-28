import random
import matplotlib.pyplot as plt
import csv
import Main_test
import Testing

main_function = Main_test.Tests
data = Testing.data
""" ---------- Semester work -----------------"""
"""
Task:
1) Generating of start positions
2) Implementation of objects: pedestrian, vehicle, rider
3) Implementation of methods: time of accident and place of accident
4) Grafical results
5) Data exports to CSV file
"""

class Final:
    def testing(self):
        result_time = []
        result_place = []
        j = random.randint(0, len(data))
        m = random.randint(0, len(data))
        if j != m:
            pass
        else:
            m = random.randint(0, len(data))
        #print(m, j)
        for i in range(0, 10):
            test = main_function
            a = test.timer(test, data[j].position, data[m].position, data[j].speed, data[m].speed)
            b = test.place_issue(test, data[j].speed, a)
            result_time.append(a)
            result_place.append(b)
            j = random.randint(0, len(data)-1)
            m = random.randint(0, len(data)-1)
        return result_time, result_place

test_results = Final().testing()


class Graphs:
    def generate_graphs(self):
        # grafical interpretation of data
        names = range(1, 11)
        values = test_results[1]
        plt.figure(figsize=(12, 5))
        plt.scatter(names, values)
        plt.ylabel("Place of accident")
        plt.xlabel("Number of test situation")
        plt.axis([0, 10, 0, 1000])
        plt.title('Place of colision')

        names = range(1, 11)
        values = test_results[0]
        plt.figure(figsize=(12, 5))
        plt.scatter(names, values)
        plt.axis([0, 10, 0, 30])
        plt.ylabel("Time of accident")
        plt.xlabel("Number of testcase")
        plt.title('Time of colision')
        plt.show()

graphs = Graphs().generate_graphs()

class Export:
    def export(self):
        # exports data to CSV
        with open('Data_export', 'w') as f:
            fields = ['Number of testcase', 'Time of colision [s]', 'Place of colision [m]']
            write = csv.writer(f)
            write.writerow(fields)
            for i in range(0, 10):
                rows = [(i, test_results[0][i], test_results[1][i])]
                write.writerows(rows)
export = Export().export()



