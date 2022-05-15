
# Find The Largest Product adjacent pair of the list

def solution(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
  
  # max is a keyword which find the maximum number in a group numbers
  # inside max( Parenthesis this form a list of number which is product of adjacent pairt o inputArray elements)
