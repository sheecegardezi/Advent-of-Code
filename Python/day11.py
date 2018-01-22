#convert the input text into python datastructure
#return [list,of,numbers,......]
def extractDataStructure():
    
    dataStructure=[]
    file = open("input/day11.txt", "r")
    
    for line in file:
        for letter in line:
            dataStructure.append(int(letter))
        
    return dataStructure

#main program
dataStructure=extractDataStructure()

answer=0

#add current value to answer if the value exact half distance of length of array in equal to the current value
for i in range(0,len(dataStructure)-int(len(dataStructure)/2)):
    if dataStructure[i] == dataStructure[i+int(len(dataStructure)/2)]:
        answer=answer+dataStructure[i]
        
#comapre the late half of the data with the starting data
for i in range(len(dataStructure)-int(len(dataStructure)/2),len(dataStructure)):
    if dataStructure[i-len(dataStructure)+int(len(dataStructure)/2)] == dataStructure[i]:
        answer=answer+dataStructure[i]
    
#output
print(answer)
