import csv
import datetime
import numpy
import sys

#print ('Argument List:', str(sys.argv[1]))

exampleFile = open(str(sys.argv[1]))
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


def normalize(v):

   return(list(numpy.asarray(v) - min(v)))	

def countFive(list,no):

	cou=0
	listFive=[]
	#cou2=0
	
	for i in range(min(list),max(list),no):
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

def interp():

	lis=[]

	for i in range (len(exampleData)):
		lis.append(exampleData[i][0])

	a=lis


	rang=int(a[-1])-int(a[0])
	le=len(a)
	
	fact=float(rang)/le
	#print(fact)

	b=[]
	b.append(a[0])
	for i in range (len(a)):
		b.append(int(round(int(b[i])+fact)))

	return b

def timeWrite():
	lis=[]
	for i in range (len(exampleData)):
		#lis.append(int(int(exampleData[i][0])/1000))

		lis.append(datetime.datetime.fromtimestamp(int(exampleData[i][0])/1000).strftime('%Y-%m-%d %H:%M:%S'))
	return(lis)

def timeRange(val):

	indexTimeVal=listTimeSplitDecide.index(val)+1
	return(listTimeSplitDecide[indexTimeVal])

def getCollumn(c):
	cc=[]
	for i in range(len(exampleData)):
		cc.append((exampleData[i][c]))
	return cc

def addingTimeRanges():

	lstTimeRange=[]
	for i in range (len(exampleData)):
		tmp1=listTime[i]
		#print(timeRange(tmp1))
		lstTimeRange.append(timeRange(tmp1))

	return lstTimeRange


	

listTime=timeF()
listTimeSplitDecide=(countFive(listTime,5))
timeWriteOut=timeWrite()
interPol=interp()
timeRange=addingTimeRanges()

xNorm=normalize(list(map(float, getCollumn(1))))
yNorm=normalize(list(map(float, getCollumn(2))))
zNorm=normalize(list(map(float, getCollumn(3))))


outputFileName=str(sys.argv[1])[:-4]+"_v2.csv"


#outputFile = open('output.csv', 'w')
with open(outputFileName, 'w', newline='') as outfile:
	outputWriter = csv.writer(outfile)

	t="timeStamp","x","y","z","second","timeGroup","dateTime","timeInter","xNorm","yNorm","zNorm"
	outputWriter.writerow(t)

	for i in range (len(exampleData)):
		strTem=[exampleData[i][0],
		exampleData[i][1],
		exampleData[i][2],
		exampleData[i][3],
		listTime[i],
		timeRange[i],
		timeWriteOut[i],
		interPol[i],
		xNorm[i],
		yNorm[i],
		zNorm[i]]


		outputWriter.writerow(strTem)


#------write the time to file end -------------------------