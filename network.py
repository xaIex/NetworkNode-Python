import random
import numpy as np

def deltaFunction(v):
    alpha = 5 # constant
    return 1 / (1 + np.exp(-alpha * v))

def getZ0_N0(num):
    if(num == 1):
        return 1, 1
    elif(num == 2):
        return 0.5, 2
    elif(num == 3):
        return 1/3, 3
    elif(num == 4):
        return 0.25, 4
    else:
        return 0.2, 5
    
def getThreshold(numArrows):
    threshold = [random.randint(0,1) for _ in range(numArrows)]
    return threshold

def getBias(numArrows):
    bias = [random.random() for _ in range(numArrows)]
    return bias

def calculateNode(x, tau, bias, z0, n0):
    # x (inputs) - xi | bias - bi | tau (threshold) - ti | n0, z0 
    N = len(x) 
    # calculating the sum from i to N (length of inputs x)
    zSum = 0
    for i in range(N):
        # calculate v delta function then pass to deltaFunction 
        # In the summation, you are only summing what is within the partheneses ()
        v = (200 * bias[i] - 100) * (x[i] - tau[i])
        zSum += deltaFunction(v)

    z = (z0 * zSum - N + n0)

    return max(0, z)

def calculateNetwork(I1, I2):
    input = [I1, I2]

    inputThreshold1, inputBias1 = getThreshold(2), getBias(2)
    inputThreshold2, inputBias2 = getThreshold(2), getBias(2)
    inputThreshold3, inputBias3 = getThreshold(2), getBias(2)

    z0, n0 = getZ0_N0(2)

    output1 = calculateNode(input, inputThreshold1, inputBias1, z0, n0)
    output2 = calculateNode(input, inputThreshold2, inputBias2, z0, n0)
    output3 = calculateNode(input, inputThreshold3, inputBias3, z0, n0)

    outputNodes = [output1, output2, output3]

    outputThreshold1, outputBias1 = getThreshold(3), getBias(3)
    outputThreshold2, outputBias2 = getThreshold(3), getBias(3)

    z0_out, n0_out = getZ0_N0(3)

    O1 = calculateNode(outputNodes, outputThreshold1, outputBias1, z0_out, n0_out)
    O2 = calculateNode(outputNodes, outputThreshold2, outputBias2, z0_out, n0_out)
    return O1, O2

    
def runNetwork():
    print("I2 | I2 | O1 | O2\n")
    # this loops will run our inputs 00 - 11
    for I1 in [0, 1]:
        for I2 in [0,1]:
            O1, O2 = calculateNetwork(I1, I2) # get our outputs
            print(f"{I1} | {I2} | {O1:.2f} | {O2:.2f}") # print and format outputs
            
runNetwork()
