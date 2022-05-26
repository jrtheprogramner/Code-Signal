def solution(inputArray):
    m = max(len(s) for s in inputArray)
    return [s for s in inputArray if len(s) == m]
