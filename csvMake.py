import csv
import datetime

exampleFile = open('t1.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


	


def countFive(list,no):

	cou=0
	listFive=[]
	#cou2=0
	
	for i in xrange(min(list),max(list),no):
		for j in range(i,i+no):
			#print(j,cou)
			#
			listFive.append(j)
			listFive.append(cou)

			#cou2+=1
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


def interp(li):

	a=li

	t=float(a[-1]-a[0])/len(a)

	b=[]
	b.append(a[0])
	for i in range (len(a)):
		b.append(int(round(b[i]+t)))

	return b



def timeWrite():
	lis=[]
	for i in range (len(exampleData)):
		#lis.append(int(int(exampleData[i][0])/1000))

		print(datetime.datetime.fromtimestamp(int(exampleData[i][0])/1000).strftime('%Y-%m-%d %H:%M:%S'))
	return(lis)




listTime=timeF()
listTimeSplitDecide=(countFive(listTime,5))




############################# adding time range to example data
def timeRange(val):

	indexTimeVal=listTimeSplitDecide.index(val)+1
	return(listTimeSplitDecide[indexTimeVal])

lstTimeRange=[]
for i in range (len(exampleData)):
	tmp1=listTime[i]
	#print(timeRange(tmp1))
	lstTimeRange.append(timeRange(tmp1))

##################################### adding time range to example data end


outputFile = open('output.csv', 'wb')
outputWriter = csv.writer(outputFile)


for i in range (len(exampleData)):
	outputWriter.writerow([exampleData[i][0], exampleData[i][1],exampleData[i][2], exampleData[i][3],listTime[i],lstTimeRange[i]])


#------write the time to file end -------------------------