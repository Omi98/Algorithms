# python3
# a simple program to find the maximum
# score that a 'maximizing' player can get

# importing math lib for a log function
import math

# defining minimax method
# Returns the optimal value a maximizer can obtain. 
# depth is current depth in game tree. 
# nodeIndex is index of current node in scores[]. 
# isMax is true if current move is 
# of maximizer, else false 
# scores[] stores leaves of Game tree. 
# h is maximum height of Game tree 
def minimax (currentDepth, nodeIndex, maxTurn, scores, targetDepth):
  # base case: target depth reached
  # Terminating condition. i.e leaf node is reached
  # end of tree 
  if (currentDepth == targetDepth):
    return scores[nodeIndex]
  
  # If current move is maximizer, 
  # find the maximum attainable value (from the two)
  # 'max()' func. returns the maximum of the two!
  if (maxTurn):
    return max(minimax(currentDepth + 1, nodeIndex * 2, False, scores, targetDepth), minimax(currentDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

  # Else (If current move is Minimizer), 
  # find the minimum attainable value 
  # 'min()' func. returns the minimum of the two!
  else:
    return min(minimax(currentDepth + 1, nodeIndex * 2, True, scores, targetDepth), minimax(currentDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# driver code

# The number of elements 
# in scores must be a power of 2
scores = [3, 5, 2, 9, 12, 5, 23, 23]  

# A utility function to find Log n in base 2 
# (calculates tree depth)
treeDepth = math.log(len(scores), 2) 

print("The optimal value is : ", end = "") 
print(minimax(0, 0, True, scores, treeDepth)) 

# steps of max()
# - find the maximum of the two children
# - set maxTurn to false (so that next turn is min)
#
# steps of min()
# - find the minimum of the two children
# - set maxTurn to true (so that next turn is max)

# RULE:
# children of ith node: i*2, i*2+1