#convert the input text into python datastructure#[[header,[list,of,nodes],flag],...]def extractDataStructure():        dataStructure=[]    file = open("input.txt", "r")        for line in file:         nodes=[]        header=line.split(' ')[0]                if '>' in line:            RHS = line.split('>')[1]            if ',' in RHS:                nodes=RHS.split(',')                                nodes=[node.strip() for node in nodes]                            else:                nodes=RHS.strip()        dataStructure.append([header,nodes,True])            return dataStructure    
#main programdataStructure=extractDataStructure()
#check if there is a incomming link and update the flag to faslefor i in range(0,len(dataStructure)):    for j in range(0,len(dataStructure)):        if i != j:            if dataStructure[i][0] in dataStructure[j][1]:                dataStructure[i][2] = False                break            #output elemnt without incomming linkfor element in dataStructure:    if element[2] == True:        print(element)

