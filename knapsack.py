import time
import sys
import math

# this function goes through the history and prints 1 solution
def oneOptimal(weight,objectNum):
    # if the weight is zero it returns
    if weight == 0:
        return
    # the object equals the value the pair is added to the solution arry and it returns
    if(pair[objectNum][0] == holder[objectNum][weight]):
        oneSol.append(objectNum)
        return
    # if the row below this is zero than this function is called again
    elif (holder[objectNum-1][weight] == holder[objectNum][weight]):
        oneOptimal(weight,objectNum-1)
    #  if the row below the current one has a value not equal then determine if the 
    # current object should be included in the solution array
    elif (holder[objectNum-1][weight] != holder[objectNum][weight]):
        originalWeight=pair[objectNum][1]
        originalValue=pair[objectNum][0]
        otherValue=holder[objectNum-1][weight-originalWeight]
        if holder[objectNum][weight]==originalValue + otherValue:
            oneSol.append(objectNum)
        oneOptimal(weight-originalWeight,objectNum-1)
    
# function to calculate optimal value and weight 
def knapsack(n):
    # find how many objects there are
    length = len(pair)
    # make sure that the number of objects is not less than the parameter of objects to be used, n
    if n> cap:
        return
    for paired in range(length):
        # check history and make sure this value hasn't been calculated already
        if(holder[paired][0] == -1):
            for limit in range(cap+1):
                # get weights and values
                value = pair[paired][0]
                weight = pair[paired][1]
                # check that the weight doesnt go over the limit
                if(weight > limit):
                    if(paired-1>=0):
                        holder[paired][limit]= holder[paired-1][limit]
                    else:
                        holder[paired][limit]=0
                else:
                    # if the weight doesnt go over the limit then find what the local max is
                    if(paired-1>=0):
                        previous = holder[paired-1][limit]
                        current = value
                        diff = limit - weight
                        if diff > 0:
                            if(holder[paired-1][diff]+current > previous):
                                current = holder[paired-1][diff]+current
                        if current < previous:
                            holder[paired][limit] = previous
                        else:
                            holder[paired][limit] = current
                    else:
                        holder[paired][limit] = value
    knapsack(n+1)
                    
# open input file
file = open("data.txt","r")
cap = int(sys.argv[1])
array = []
# get file into correct format
test = file.read()
test = test.replace(" ", ",")
test = test.replace("\n", ",")
test = test.split(",")
test = [int(i) for i in test]
odd=[]
even=[]
j = 0
# split lines into their values and weights
for i in test:
    if (j % 2) == 0:
        even.append(i)
    else:
        odd.append(i)
    j=j+1
j = 0
pair =[]
for i in odd:
    pair.append((i,even[j]))
    j = j+1
# sort array
sortedPair = pair.sort(key=lambda x : x[1])
# reverse it so that highest weights at beginning of array
pair.reverse()
x = cap+1
y = len(pair)
holder = []
# making a history array
for i in range(y):
    grid2 =[]
    for i in range(x):
        grid2.append(-1)
    holder.append(grid2)
# calling recursive function
knapsack(1)
print (holder)
oneSol = []
allSol = []
# setting solution array
oneOptimal(cap,y-1)
oneSolLength = len(oneSol)
# printing solution
print("Optimal Subset")
for z in range(oneSolLength):
    print("Value",pair[oneSol[z]][0],"Weight",pair[oneSol[z]][1])
