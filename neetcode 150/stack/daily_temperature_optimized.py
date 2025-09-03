class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myTemps = []           # stack of indices
        ans = [0]*len(temperatures)

        for x in range(len(temperatures)):
            # While current temp is warmer than the temp at the stack's top index,
            # pop that index and set its answer to the distance to 'x'
            while myTemps and temperatures[x] > temperatures[myTemps[-1]]:
                pos = myTemps.pop()
                ans[pos] = x - pos

            # Push current index; its answer is not known yet
            myTemps.append(x)

        return ans