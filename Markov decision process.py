import numpy as np
from numpy import double
import string


frelist=[[7, 1], [12, 1], [3, 1]]
frelist=np.array(frelist)
i=0
j=2
frelist[[i, j], :] = frelist[[j, i], :]
print(frelist)


def pi_V():
    Ppi = [None for i in range(81)]
    for i in range(81):
        Ppi[i] = Pass[pi[i]][i]
    Ppi = np.array(Ppi)
    A = np.array(np.identity(81)) - gama * np.array(Ppi)
    val = np.linalg.solve(A, np.array(R))
    return val


def Qval(s, a):
    prob = Pass[a][s]
    sum = 0;
    for i in range(len(prob)):
        if prob[i] != 0:
            sum += prob[i] * val[i]
    return sum


# policy iteration
def Policy_iteration():
    # this was done by solve equation as whole,
    # thus no need to create new array
    for s in range(81):
        max = Qval(s, 0)
        direct = 0
        for t in range(1, 4):
            thisQ = Qval(s, t)
            if max < thisQ:
                max = thisQ
                direct = t
        pi[s] = direct


# value iteration
def Value_iteration():
    # create a new array for value
    newvalue = [0 for i in range(81)]
    for s in range(81):
        max = Qval(s, 0)
        direct = 0
        for t in range(1, 4):
            thisQ = Qval(s, t)
            if max < thisQ:
                max = thisQ
                direct = t
        newvalue[s] = gama * max + R[s]
    return newvalue


def list_matrix(list):
    list2d = [[0 for i in range(9)] for j in range(9)]
    for i in range(81):
        row = (int)(i / 9)
        col = i % 9
        list2d[col][row] = list[i]
    return np.matrix(list2d)


Pass = [[[0 for i in range(81)] for k in range(81)] for j in range(4)]

for t in range(1, 5):
    filename = '../prob_a' + str(t) + '.txt'
    with open(filename) as file:
        line_s = file.readlines()
    for i in range(len(line_s)):
        line = line_s[i].replace("\n", "")
        numstr = line.split("  ")
        a1 = int(numstr[0]) - 1
        a2 = int(numstr[1]) - 1
        prob = double(numstr[2])
        # print(t,a1,a2)
        Pass[t - 1][a1][a2] = prob

R = [None for i in range(81)]
with open('../rewards.txt') as file:
    line_s = file.readlines()
for i in range(len(line_s)):
    line = line_s[i].replace("\n", "")
    R[i] = int(line)

# print(reward)

valid = [3, 11, 12, 15, 16, 17,
         20, 22, 23, 24, 26,
         29, 30, 31, 34, 35,
         39, 43, 48, 52, 53,
         56, 57, 58, 59, 60, 61, 62,
         66, 70, 71, 100]  # add extra to avoid overfloat
"""
# examine the non-zero value
print("examine the non-zero value")

for i in valid:
    print("___for  ", i)
    for t in range(4):
        print("_", (t + 1))
        line = Pass[t][i - 1]
        for j in range(len(line)):
            if line[j]!=0:
                print(j + 1, "\t", line[j])
"""

# policy iteration

val = [0 for i in range(81)]
pi = [0 for i in range(81)]
gama = 0.9925
""""""
for i in range(100):
    val = pi_V()
    # print("____times__",i)
    Policy_iteration()
print("=========policy iteration=========")
np.set_printoptions(precision=2)
print(list_matrix(val))

# print the policy
# print(u'\u2190',u'\u2191',u'\u2192',u'\u2193')
print("=========optimal policy=========")
directstr = [[" " for i in range(9)] for j in range(9)]
now = 0
for i in range(81):
    row = int(i / 9)
    col = i % 9
    thisstr = ""
    if i + 1 == valid[now]:
        if pi[i] == 0:
            thisstr = u'\u2190'
            # print(u'\u2190', "\t", end='')
        elif pi[i] == 1:
            thisstr = u'\u2191'
            # print(u'\u2191', "\t", end='')
        elif pi[i] == 2:
            thisstr = u'\u2192'
            # print(u'\u2192', "\t", end='')
        elif pi[i] == 3:
            thisstr = u'\u2193'
            # print(u'\u2193', "\t", end='')
        now += 1
        directstr[col][row] = thisstr
    # else:
    # print("\t", end='')
    # if (i+1) % 9==0:
    # print()
# print
for i in range(9):
    for j in range(9):
        print(directstr[i][j], "\t", end="")
    print()

val = [0 for i in range(81)]
pi = [0 for i in range(81)]
# this converge much slow than the policy iteration,
# although much less computation in each iteration
for i in range(10000):  # 10000>100
    # print("____times__",i)
    val = Value_iteration()
    # print(val)
print("==========value iteration==========")
np.set_printoptions(precision=2)
print(list_matrix(val))
