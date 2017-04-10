import csv
import datetime

exampleFile = open('t1.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


	


def countFive(list,no):

	cou=0
	listFive=[]
	cou2=0

	for i in xrange(min(list),max(list),no):
		for j in range(i,i+no):
			#print(j,cou)
			listFive.append([])
			listFive[cou2].append(j)
			listFive[cou2].append(cou)

			cou2+=1
		cou+=1

	return (listFive)




def timeF():

	lis=[]
	for i in range (len(exampleData)):
		lis.append(int(exampleData[i][0]))
	#print(exampleData[i][0])
	#time(exampleData[i][0])

	lis2=[]
	for i in range (len(exampleData)):
		lis2.append(int(datetime.datetime.fromtimestamp(lis[i]/1000).strftime('%M'))*60+int(datetime.datetime.fromtimestamp(lis[i]/1000).strftime('%S')))

	return(lis2)

print(countFive(timeF(), 5))


