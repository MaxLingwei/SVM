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
    fp.close()
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
    fp.close()
    return label

def svm_output(w, b, x):
    sum = 0
    for j in range(0, len(w)):
        sum += w[j] * x[j]
    sum += b
    return sum

def funL(w, b, x, y):
    out = 1 - y * svm_output(w, b, x)
    return max(0, out)

def normfun(w):
    sum = 0
    for j in range(0, len(w)):
        sum += w[j] * w[j]

    return float(sum) / 2

def costfun(w, b, x, y, C):
    sum = 0
    for i in range(0, len(y)):
        sum += funL(w, b, x[i], y[i])
    return normfun(w) + C * sum

def deri_L_wj(w, b, x, y, j):
    if y * svm_output(w, b, x) >= 1:
        return 0
    else:
        return -y * x[j]

def deri_L_b(w, b, x, y):
    if y * svm_output(w, b, x) >= 1:
        return 0
    else:
        return -y

def deri_f_wj(w, b, C, x, y, j):
    sum = 0
    for i in range(0, len(y)):
        sum += deri_L_wj(w, b, x[i], y[i], j)
    sum += w[j]
    return sum

def deri_f_b(w, b, C, x, y):
    sum = 0
    for i in range(0, len(y)):
        sum += deri_L_b(w, b, x[i], y[i])
    return C * sum
    
def writeFile(filename, data):
    fp = open(filename, 'w')
    for i in range(0, len(data)):
        fp.write(str(data[i]) + '\n')
    fp.close()

def train(w, b, x, y, C, eta, epsilon):
    delta_cost = 10
    iter_num = 0
    error_k_1 = 0
    error_k = 0
    delta_cost_set = []
    error_set = []

    while delta_cost > epsilon:
        print iter_num
        error_k_1 = costfun(w, b, x, y, C)
        print error_k_1
        error_set.append(error_k_1)
        for j in range(0, len(w)):
            w[j] -= eta * deri_f_wj(w, b, C, x, y, j)
        b -= eta * deri_f_b(w, b, C, x, y)
        error_k = costfun(w, b, x, y, C)
        delta_cost = 100 * abs(error_k - error_k_1) / error_k_1
        delta_cost_set.append(delta_cost)
        print delta_cost
        iter_num += 1
    writeFile('delta_cost.txt', delta_cost_set)
    writeFile('error.txt', error_set)

if __name__ == '__main__':
    #initial
    feature = readFeature('features.txt')
    label = readLabel('target.txt')

    dimension = len(feature[0])
    w = [0] * dimension
    b = 0
    eta = 3e-7
    epsilon = 0.25
    C = 1

    train(w, b, feature, label, C, eta, epsilon)
