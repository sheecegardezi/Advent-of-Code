#convert the input text into python datastructure
#return [[list,of,numbers,......],[...],...]
def extractDataStructure():
    
    dataStructure=[]
    file = open("input/day21.txt", "r")
    
    for line in file:
        row=[]
        for letter in line.split('\t'):
            row.append(int(letter))
        dataStructure.append(row)
        
    return dataStructure


#main program
dataStructure=extractDataStructure()

#sum the difference between max and min value of each row
answer = 0

#dividend
for row in dataStructure:
    for i in range(0,len(row)):
        #divisor
        for j in range(0,len(row)):
            #check if the index is not same i.e. same number
            if i !=j:
                if row[i]%row[j]==0:
                    answer=answer+row[i]/row[j]
#output
print(answer)
