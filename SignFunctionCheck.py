import os
import sys
import numpy as np
import matplotlib.pyplot as plt


class SignFunction:
    def __init__(self):
        # self.dayTime = 24*3600
        self.timeRatio = 60
        self.dayTime = 24*self.timeRatio
        self.timeArr = np.arange(0, self.dayTime, 1)

    def getExpectedStateFunc(self, ruleStartTime, ruleStopTime):
        output = []
        for t in range(0, self.dayTime):
            op = (np.sign(-(t - ruleStartTime)*(t - ruleStopTime)) +
                  np.sign(abs((ruleStopTime - t)*(ruleStartTime - t))))/2
            output.append(op)
        return output

    def getUnexpectedStateFunction(self, ruleState, rulePriority):
        output = []     
        for t in range(0, self.dayTime):
            j = np.complex_(1j)
            op = ruleState*rulePriority*j
            output.append(op)
        return output

    def combineTwoFunc(self, firstFunc, secFunc):
        output = []
        for t in range(0, self.dayTime):
            op = firstFunc[t] + secFunc[t]
            output.append(op)
        return output

    def conflictCheck(self, deviceState):
        complexCheck = str(deviceState).find('j')
        output = []
        if complexCheck == -1:
            return deviceState
        else:
            for state in deviceState:
                if (np.imag(state**2) > 1):
                    op = -1
                else:
                    op = abs(np.real(state**2))
                output.append(op)
            return output

    def plottingData(self, plotName, x_arr, y_arr):
        print("Plotting data...")
        plt.title(plotName)
        for i in range(0, self.dayTime):
            plt.plot(x_arr[i:i+2], y_arr[i:i+2], 'r-')
        plt.show()

    def run(self):
        arr_1 = self.getExpectedStateFunc(5*self.timeRatio, 12*self.timeRatio)
        # arr_2 = self.getUnexpectedStateFunction(1,1)
        arr_2 = self.getExpectedStateFunc(15*self.timeRatio, 20*self.timeRatio)
        deviceState = self.combineTwoFunc(arr_1,arr_2)
        # deviceState = arr_2
        op = self.conflictCheck(deviceState)
        # y_arr = self.getExpectedStateFunc(5*self.timeRatio, 12*self.timeRatio)
        # y_arr = signFunction.getUnexpectedStateFunction(1,1)
        x_arr = self.timeArr
        y_arr = op
        self.plottingData('Sign Function', x_arr, y_arr)


if __name__ == '__main__':
    print("Calculating...")
    signFunction = SignFunction()
    signFunction.run()
    # signFunction.getUnexpectedStateFunction(1,1)
