import itertools


# Python program to get equivalent resistance
def getEquivalentR(myList) :
    
    # Multiply elements one by one 
    result = 0
    for x in myList: 
         result = result + 1/x  
    return 1/result  


###############################################################
#get resistances that will be used in parallel
endFlag = False
counter = 1
lst = []
while endFlag == False:
    #ask for user input. Repeat if user input is invalid
    flag = False
    while flag == False:
        g = input("Enter resistance " + str(counter) + " (-1 to stop): ")
        
        try:
            # convert parsed input to integer
            g = int(g)
            flag = True
            #insure that the user input is a valid index in the list
            if g <= 0:
                endFlag = True
            else:
                lst.append(g)
                counter += 1
        except:
            print("input must be a positive number")
            flag = False
            

#run through all combinations and find the equivalence resistance

for x in range(len(lst)):
    print("pressing (" + str(lst[x]) + ") = " + str(lst[x]))
for x in range(2, len(lst)+1):
    tmp = list(itertools.combinations(lst, r=x))
    for y in range(len(tmp)):
        print("pressing " + str(tmp[y]) + " = " + str(getEquivalentR(tmp[y])))
            
input("press enter to continue...")
