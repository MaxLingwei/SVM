import matplotlib.pyplot as plt

def readData(filename):
    data = []
    fp = open(filename, 'r')
    while 1:
        line = fp.readline()
        if not line:
            break
        line = float(line)
        data.append(line)
    fp.close()
    return data

if __name__ == '__main__':
    data = readData('error.txt')
    plt.plot(data)
    plt.show()
