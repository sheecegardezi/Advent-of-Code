#convert the input text into python datastructure
#return [list,of,numbers,......]
def extractDataStructure():
    
    dataStructure=[]
    file = open("input/day1.txt", "r")
    
    for line in file:
        for letter in line:
            dataStructure.append(int(letter))
        
    return dataStructure

#main program
dataStructure=extractDataStructure()

answer=0

#add current value to answer if the next value in equal to the current value
for i in range(0,len(dataStructure)-1):
    if dataStructure[i] == dataStructure[i+1]:
        answer=answer+dataStructure[i]
#handle last element
if dataStructure[0] == dataStructure[-1]:
    answer=answer+dataStructure[0]
    
#output
print(answer)
