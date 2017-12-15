#convert the input text into python datastructure#return [list,of,numbers,......]def extractDataStructure():        dataStructure=[]    file = open("input/day1.txt", "r")        for line in file:        for letter in line:            dataStructure.append(int(letter))            return dataStructure
#main programdataStructure=extractDataStructure()
answer=0
#add current value to answer if the next value in equal to the current valuefor i in range(0,len(dataStructure)-1):    if dataStructure[i] == dataStructure[i+1]:        answer=answer+dataStructure[i]#handle last elementif dataStructure[0] == dataStructure[-1]:    answer=answer+dataStructure[0]    #outputprint(answer)
