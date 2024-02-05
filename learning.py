Import numpy as np


def cross_entropy(Y, P):
    print(Y)
    print(P)
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


print(cross_entropy([1, 1], [0.4, 0.5]))

B
C
in
