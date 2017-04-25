
def readFeature(filename):
    feature = []
    fp = open(filename, 'r')
    while 1:
        line = fp.readline()
        if not line:
            break
        line = line.split(',')
        for i in range(0, len(line)):
            line[i] = int(line[i])
        feature.append(line)
    return feature


def readLabel(filename):
    label = []
    fp = open(filename, 'r')
    while 1:
        line = fp.readline()
        if not line:
            break
        line = int(line)
        label.append(line)
    return label

def svm_output(w, b, x):
    sum = 0
    for i in range(0, len(w)):
        sum += w[i] * x[i]
    sum += b
    return sum

def funL(w, b, x, y):
    out = 1 - y * svm_output(w, x, b)
    return max(0, out)

def normfun(w):
    sum = 0
    for i in range(0, len(w)):
        sum += w[i] * w[i]

    return float(sum) / 2

def costfun(w, b, x, y, C):

