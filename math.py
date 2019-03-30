from random import randint
from collections import Counter
import math

def get_data(filename):
    # DATA FORMAT:
    # data1
    # data2
    # data3
    data = []
    with open(filename, 'r') as f:
        data = f.read().split('\n')
        data = [int(data) for data in data]
    return data

def get_mean(data):
    mean = sum([data for data in data]) / len(data)
    return mean

def get_table(data):
    table = dict(Counter(data))
    return table

def get_mode(table):
    mode = {}
    max_occurs = 0
    # Key is the data, v is how many occurencces of the data is in the data set. Also known as frequency.
    for k, v in table.items():
        if v > max_occurs:
            max_occurs = v
            mode = {k: v}
        if v == max_occurs:
            mode.setdefault(k, v)
    return mode    
    
def get_dispersion_table(table, mean):
    dispersion_table = {}
    for x, f in table.items():
        # x is the data number. Idk whats it called and f is frequency, or occurences.
        x = int(x)
        second = abs(mean-x)
        third = second ** 2
        forth = f * third
        dispersion_table.setdefault(
            x, {'x': x, 'f': f, 'second': second, 'third': third, 'forth': forth})
    return dispersion_table
    
def get_total(table):
    total = 0
    for v in table.values():
        total += v['forth']
    return total

def get_range(data):
    # range is a reserved keyword.
    rangee = max(data) - min(data)
    return rangee

def get_variance(data, total):
    variance = total / (len(data) - 1)
    return variance

def get_standard_deviation(variance):
    # square root
    return variance ** 0.5

def print_data(data):
    print("List of the Data:")
    i = 0
    j = int(len(data) / 2)
    limit = j
    if len(data) % 2 != 0:
        j = len(data) // 2 + 1
    while i < limit:
        print(str(i + 1) + ".) " + str(data[i]),"\t", str(j + 1) + ".) " + str(data[j]))
        i += 1
        j += 1
    return

def print_table(table):
    print("Table: Where F is frequency and X is the data.")
    print("===============")
    print("|  X   |   F  |")
    print("====== | ======")
    for k, v in table.items():
        print("|" + str(k).center(6) + "|" + str(v).center(6) + "|")
    print("===============")
    return

def print_mode(mode):
    print("Mode(s):")
    keys = ""
    v = ""
    for k, v in mode.items():
        keys =  str(k) + keys
        v = str(v)
    print(keys + " with a frequency of " + v + ".")

def print_dispersion_table(table):
    print("Dispersion Table: Where x is the data, f is frequency and m is mean.")
    print("===========================================")
    print("|  x  |  f  | m-x  | (m-x)^2 | f((m-x)^2) |")
    print("===========================================")
    for item in table.values():
        x = str(item['x'])
        f = str(item['f'])
        second = str(round(item['second'], 2))
        third = str(round(item['third'], 2))
        forth = str(round(item['forth'], 2))
        print(
            "|" + x.center(5) + "|" + f.center(5) + "|" + second.center(6) + "|" + third.center(9) + "|" + forth.center(12) + "|")
    print("===========================================")
    return


def main(filename):
    data = get_data(filename)
    mean = get_mean(data)
    table = get_table(data)
    mode = get_mode(table)
    dispersion_table = get_dispersion_table(table, mean)
    total = get_total(dispersion_table)
    rangee = get_range(data)
    variance = get_variance(data, total)
    standard_deviation = get_standard_deviation(variance)

    print("=" * 19 + "START" + "=" * 19)
    print("Filename: {}".format(filename))
    print_data(data)
    print("\nMean: {}".format(mean))
    print_table(table)
    print_mode(mode)    
    print_dispersion_table(dispersion_table)
    print("Total: {}".format(total))
    print("Range: {}".format(rangee))
    print("Variance: {}".format(variance))
    print("Standard Deviation: {}".format(standard_deviation))
    print("=" * 20 + "END" + "=" * 20)

if __name__ == "__main__":
    filename = 'phone.txt'
    main(filename)
