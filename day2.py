#convert the input text into python datastructure#return [[list,of,numbers,......],[...],...]def extractDataStructure():        dataStructure=[]    file = open("input/day2.txt", "r")        for line in file:        row=[]        for letter in line.split('\t'):            row.append(int(letter))        dataStructure.append(row)            return dataStructure
#main programdataStructure=extractDataStructure()
#sum the difference between max and min value of each rowanswer= sum ([ max(row)-min(row) for row in dataStructure ])
#outputprint(answer)
